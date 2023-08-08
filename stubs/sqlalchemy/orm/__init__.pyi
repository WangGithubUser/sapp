from typing import Any, Optional

from . import mapper as mapperlib
from .descriptor_props import (
    ComparableProperty as ComparableProperty,
    CompositeProperty as CompositeProperty,
    SynonymProperty as SynonymProperty,
)
from .interfaces import (
    EXT_CONTINUE as EXT_CONTINUE,
    EXT_STOP as EXT_STOP,
    PropComparator as PropComparator,
)
from .mapper import (
    class_mapper as class_mapper,
    configure_mappers as configure_mappers,
    Mapper as Mapper,
    reconstructor as reconstructor,
    validates as validates,
)
from .properties import ColumnProperty as ColumnProperty
from .query import AliasOption as AliasOption, Bundle as Bundle, Query as Query
from .relationships import (
    foreign as foreign,
    RelationshipProperty as RelationshipProperty,
    remote as remote,
)
from .scoping import scoped_session as scoped_session
from .session import (
    make_transient as make_transient,
    make_transient_to_detached as make_transient_to_detached,
    object_session as object_session,
    Session as Session,
    sessionmaker as sessionmaker,
)
from .strategy_options import Load as Load
from .util import (
    aliased as aliased,
    join as join,
    object_mapper as object_mapper,
    outerjoin as outerjoin,
    polymorphic_union as polymorphic_union,
    was_deleted as was_deleted,
    with_parent as with_parent,
    with_polymorphic as with_polymorphic,
)

def create_session(bind: Optional[Any] = ..., **kwargs): ...

relationship = RelationshipProperty

def relation(*arg, **kw): ...
def dynamic_loader(argument, **kw): ...

column_property = ColumnProperty
composite = CompositeProperty

def query_expression() -> ColumnProperty: ...
def backref(name, **kwargs): ...
def deferred(*columns, **kw): ...

mapper = Mapper
synonym = SynonymProperty
comparable_property = ComparableProperty

def compile_mappers(): ...
def clear_mappers(): ...

# TODO: these are function "aliases"
joinedload: Any = ...
joinedload_all: Any = ...
contains_eager: Any = ...
defer: Any = ...
undefer: Any = ...
undefer_group: Any = ...
with_expression: Any = ...
load_only: Any = ...
lazyload: Any = ...
lazyload_all: Any = ...
subqueryload: Any = ...
subqueryload_all: Any = ...
selectinload: Any = ...
selectinload_all: Any = ...
immediateload: Any = ...
noload: Any = ...
raiseload: Any = ...
defaultload: Any = ...
selectin_polymorphic: Any = ...

def eagerload(*args, **kwargs): ...
def eagerload_all(*args, **kwargs): ...

contains_alias = AliasOption
