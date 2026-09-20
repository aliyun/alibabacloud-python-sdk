# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        engine: str = None,
    ):
        # The supported language. Valid values:
        # 
        # - **zh-CN**: Chinese (default)
        # - **en-US**: English
        # - **ja**: Japanese.
        self.accept_language = accept_language
        # The data engine type. Valid values:
        # - **hbase**: ApsaraDB for HBase Standard Edition or ApsaraDB for HBase single-node edition.
        # - **hbaseue**: ApsaraDB for HBase Performance-enhanced Edition.
        # - **serverlesshbase**: ApsaraDB for HBase Serverless edition.
        # - **bds**: BDS instance.
        self.engine = engine

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.engine is not None:
            result['Engine'] = self.engine

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        return self

