VENV = source .venv/bin/activate

.venv:
ifeq (, $(shell which uv))
	$(error uv is not installed, please install it from https://github.com/astral-sh/uv/tree/main?tab=readme-ov-file#getting-started)
endif
	@uv venv

requirements.txt: requirements.in .venv
	@$(VENV); \
		uv pip compile -o requirements.txt requirements.in && \
		uv pip sync requirements.txt
