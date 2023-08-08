# Stubs for sqlalchemy.dialects.mysql.mysqlconnector (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from .base import (
    BIT as BIT,
    MySQLCompiler as MySQLCompiler,
    MySQLDialect as MySQLDialect,
    MySQLExecutionContext as MySQLExecutionContext,
    MySQLIdentifierPreparer as MySQLIdentifierPreparer,
)

class MySQLExecutionContext_mysqlconnector(MySQLExecutionContext):
    def get_lastrowid(self): ...

class MySQLCompiler_mysqlconnector(MySQLCompiler):
    def visit_mod_binary(self, binary, operator, **kw): ...
    def post_process_text(self, text): ...
    def escape_literal_column(self, text): ...

class MySQLIdentifierPreparer_mysqlconnector(MySQLIdentifierPreparer): ...

class _myconnpyBIT(BIT):
    def result_processor(self, dialect, coltype): ...

class MySQLDialect_mysqlconnector(MySQLDialect):
    driver: str = ...
    supports_unicode_binds: bool = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    supports_native_decimal: bool = ...
    default_paramstyle: str = ...
    execution_ctx_cls: Any = ...
    statement_compiler: Any = ...
    preparer: Any = ...
    colspecs: Any = ...
    @property
    def supports_unicode_statements(self): ...
    @classmethod
    def dbapi(cls): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect: Any = ...
