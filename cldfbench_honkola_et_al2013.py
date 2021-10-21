import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "honkola_et_al2013"

    def cmd_makecldf(self, args):
        """
summary.trees: original/Ura100_beast.tre
	nexus trees -c -t $< -o $@

posterior.trees: original/Ura100_beast_full.trees.gz
	nexus trees -c -d 1-200 $< -o tmp
	nexus trees -n 1000 tmp -o $@
	rm tmp
        """
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / 'Ura100_beast.tre',
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.remove_burnin(
                self.read_gzipped_text(self.raw_dir / 'Ura100_beast_full.trees.gz'), 200),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))
