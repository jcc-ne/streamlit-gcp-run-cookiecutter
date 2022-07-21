#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the GNU GPLv3 license.

"""

"""

from .config import (
    DATABASE_HOST,
    DATABASE_HOST_REPLICA,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_NAME,
)
import sqlalchemy


db_lookup = {"default": DATABASE_HOST, "replica": DATABASE_HOST_REPLICA}


def get_url(db=None):
    host_ = db_lookup.get(db, DATABASE_HOST)
    return sqlalchemy.engine.url.URL.create(
        drivername="postgresql+psycopg2",
        host=host_,
        username=DATABASE_USER,
        password=DATABASE_PASSWORD,
        port=DATABASE_PORT,
        database=DATABASE_NAME,
    )


def get_engine(db=None):
    return sqlalchemy.create_engine(get_url(db=db))
