cat Pipfile.lock | jq '.[]."scikit-learn"."hashes"[0]'