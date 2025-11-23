help:
	@echo
	@echo "install                            -- install backend dependencies"
	@echo "lint                               -- lint backend"
	@echo "format                             -- format backend"

	@echo


.PHONY: install
install:
	uv sync --frozen

.PHONY: lint
lint:
	uv run ruff check .

.PHONY: mypy
mypy:
	 uv run mypy .

.PHONY: format
format:
	uv run ruff check --fix .
	uv run ruff format .

