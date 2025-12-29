# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class SearchStrategy(DaraModel):
    def __init__(
        self,
        description: str = None,
        is_default: bool = None,
        merge_config: main_models.SearchStrategyMergeConfig = None,
        name: str = None,
        search_configs: List[main_models.SearchStrategySearchConfigs] = None,
    ):
        self.description = description
        self.is_default = is_default
        self.merge_config = merge_config
        self.name = name
        self.search_configs = search_configs

    def validate(self):
        if self.merge_config:
            self.merge_config.validate()
        if self.search_configs:
            for v1 in self.search_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.merge_config is not None:
            result['mergeConfig'] = self.merge_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        result['searchConfigs'] = []
        if self.search_configs is not None:
            for k1 in self.search_configs:
                result['searchConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('mergeConfig') is not None:
            temp_model = main_models.SearchStrategyMergeConfig()
            self.merge_config = temp_model.from_map(m.get('mergeConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        self.search_configs = []
        if m.get('searchConfigs') is not None:
            for k1 in m.get('searchConfigs'):
                temp_model = main_models.SearchStrategySearchConfigs()
                self.search_configs.append(temp_model.from_map(k1))

        return self

class SearchStrategySearchConfigs(DaraModel):
    def __init__(
        self,
        first_rank_name: str = None,
        merge_proportion: int = None,
        query_type: str = None,
        second_rank_name: str = None,
    ):
        self.first_rank_name = first_rank_name
        self.merge_proportion = merge_proportion
        self.query_type = query_type
        self.second_rank_name = second_rank_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_rank_name is not None:
            result['firstRankName'] = self.first_rank_name

        if self.merge_proportion is not None:
            result['mergeProportion'] = self.merge_proportion

        if self.query_type is not None:
            result['queryType'] = self.query_type

        if self.second_rank_name is not None:
            result['secondRankName'] = self.second_rank_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstRankName') is not None:
            self.first_rank_name = m.get('firstRankName')

        if m.get('mergeProportion') is not None:
            self.merge_proportion = m.get('mergeProportion')

        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')

        if m.get('secondRankName') is not None:
            self.second_rank_name = m.get('secondRankName')

        return self

class SearchStrategyMergeConfig(DaraModel):
    def __init__(
        self,
        doc_count: int = None,
        rank_name: str = None,
    ):
        self.doc_count = doc_count
        self.rank_name = rank_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_count is not None:
            result['docCount'] = self.doc_count

        if self.rank_name is not None:
            result['rankName'] = self.rank_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docCount') is not None:
            self.doc_count = m.get('docCount')

        if m.get('rankName') is not None:
            self.rank_name = m.get('rankName')

        return self

