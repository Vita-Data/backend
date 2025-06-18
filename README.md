# Vita Data - Healthcare Backend (FastAPI/CouchDB Ready Phase-1)

## Clone the Repository

- create a new branch and send PRs
- no push to main branch directly would be accepted (branch ruleset)

```bash
git clone https://github.com/YOUR_USERNAME/vita-data-backend.git
cd vita-data-backend
git branch YOUR_BRANCH_NAME
git checkout YOUR_BRANCH_NAME
Add your changes
git add .
git commit -m "Your commit message"
git push -u origin YOUR_BRANCH_NAME
```

- Recommended: use a virtual environment

```bash
conda create -n vitadata python=3.10
conda activate vitadata
pip install -r requirements.txt
```

- run the app

```bash
python manage.py migrate
python manage.py runserver
```
