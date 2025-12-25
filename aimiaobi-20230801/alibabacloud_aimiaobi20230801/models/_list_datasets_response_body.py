# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListDatasetsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        custom_semantic_search_config: main_models.ListDatasetsResponseBodyCustomSemanticSearchConfig = None,
        data: List[main_models.ListDatasetsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        third_search_config: main_models.ListDatasetsResponseBodyThirdSearchConfig = None,
        total_count: int = None,
    ):
        self.code = code
        self.custom_semantic_search_config = custom_semantic_search_config
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.third_search_config = third_search_config
        self.total_count = total_count

    def validate(self):
        if self.custom_semantic_search_config:
            self.custom_semantic_search_config.validate()
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.third_search_config:
            self.third_search_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.custom_semantic_search_config is not None:
            result['CustomSemanticSearchConfig'] = self.custom_semantic_search_config.to_map()

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.third_search_config is not None:
            result['ThirdSearchConfig'] = self.third_search_config.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CustomSemanticSearchConfig') is not None:
            temp_model = main_models.ListDatasetsResponseBodyCustomSemanticSearchConfig()
            self.custom_semantic_search_config = temp_model.from_map(m.get('CustomSemanticSearchConfig'))

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDatasetsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('ThirdSearchConfig') is not None:
            temp_model = main_models.ListDatasetsResponseBodyThirdSearchConfig()
            self.third_search_config = temp_model.from_map(m.get('ThirdSearchConfig'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDatasetsResponseBodyThirdSearchConfig(DaraModel):
    def __init__(
        self,
        dataset_quota: int = None,
        dataset_used_quota: int = None,
    ):
        self.dataset_quota = dataset_quota
        self.dataset_used_quota = dataset_used_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_quota is not None:
            result['DatasetQuota'] = self.dataset_quota

        if self.dataset_used_quota is not None:
            result['DatasetUsedQuota'] = self.dataset_used_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetQuota') is not None:
            self.dataset_quota = m.get('DatasetQuota')

        if m.get('DatasetUsedQuota') is not None:
            self.dataset_used_quota = m.get('DatasetUsedQuota')

        return self

class ListDatasetsResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        dataset_description: str = None,
        dataset_id: int = None,
        dataset_name: str = None,
        dataset_type: str = None,
        doc_used_quota: int = None,
        search_dataset_enable: int = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.dataset_description = dataset_description
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.dataset_type = dataset_type
        self.doc_used_quota = doc_used_quota
        self.search_dataset_enable = search_dataset_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.doc_used_quota is not None:
            result['DocUsedQuota'] = self.doc_used_quota

        if self.search_dataset_enable is not None:
            result['SearchDatasetEnable'] = self.search_dataset_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('DocUsedQuota') is not None:
            self.doc_used_quota = m.get('DocUsedQuota')

        if m.get('SearchDatasetEnable') is not None:
            self.search_dataset_enable = m.get('SearchDatasetEnable')

        return self

class ListDatasetsResponseBodyCustomSemanticSearchConfig(DaraModel):
    def __init__(
        self,
        dataset_quota: int = None,
        dataset_used_quota: int = None,
        doc_quota: int = None,
        doc_used_quota: int = None,
    ):
        self.dataset_quota = dataset_quota
        self.dataset_used_quota = dataset_used_quota
        self.doc_quota = doc_quota
        self.doc_used_quota = doc_used_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_quota is not None:
            result['DatasetQuota'] = self.dataset_quota

        if self.dataset_used_quota is not None:
            result['DatasetUsedQuota'] = self.dataset_used_quota

        if self.doc_quota is not None:
            result['DocQuota'] = self.doc_quota

        if self.doc_used_quota is not None:
            result['DocUsedQuota'] = self.doc_used_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetQuota') is not None:
            self.dataset_quota = m.get('DatasetQuota')

        if m.get('DatasetUsedQuota') is not None:
            self.dataset_used_quota = m.get('DatasetUsedQuota')

        if m.get('DocQuota') is not None:
            self.doc_quota = m.get('DocQuota')

        if m.get('DocUsedQuota') is not None:
            self.doc_used_quota = m.get('DocUsedQuota')

        return self

