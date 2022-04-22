import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "honkola_et_al2013"

    def cmd_makecldf(self, args):
        self.init(args)
        
        summary = self.raw_dir.read_tree('Ura100_beast.tre', detranslate=True)
        args.writer.add_summary(summary, self.metadata, args.log)

        posterior = self.raw_dir.read_trees(
           'Ura100_beast_full.trees.gz',
           burnin=200, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)
