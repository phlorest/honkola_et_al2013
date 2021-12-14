import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "honkola_et_al2013"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree('Ura100_beast.tre', detranslate=True),
            self.metadata,
            args.log)

        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('Ura100_beast_full.trees.gz'),
                200),
            detranslate=True,
            as_nexus=True)

        args.writer.add_posterior(
            posterior.trees.trees, 
            self.metadata, 
            args.log)
