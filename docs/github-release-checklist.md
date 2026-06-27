# GitHub Release Checklist

Before publishing this repository, complete the following items.

## Required

- [ ] Choose a license for research artifacts and generated outputs.
- [ ] Update `CITATION.cff` author names and repository URL.
- [ ] Decide whether the original `artifacts/` working directory should remain public or move to `archive/`.
- [ ] Check that no private notes, credentials, or unpublished third-party documents are included.
- [ ] Confirm whether generated model outputs can be shared publicly under the selected license.

## Recommended

- [ ] Add one additional full run, preferably SRD-007.
- [ ] Add independent blinded human evaluation before manuscript submission.
- [ ] Calibrate MCDA weights or add sensitivity analysis.
- [ ] Add one or two real-world validation cases.
- [ ] Add paper draft under `paper/` once the manuscript structure is stable.

## Optional Git Commands

```bash
git init
git add .
git commit -m "Organize reservoir multi-agent benchmark repository"
git branch -M main
git remote add origin https://github.com/<USER>/<REPO>.git
git push -u origin main
```
