# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSampleDataListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeSampleDataListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10.
        self.page_size = page_size
        # Returned object
        self.result_object = result_object
        # Total number of items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeSampleDataListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeSampleDataListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        classification_type: str = None,
        data_distributed: str = None,
        data_title: str = None,
        delete_tag: str = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        name: str = None,
        normal_size: int = None,
        recall_config: str = None,
        risk_size: int = None,
        risk_value: str = None,
        sample_label_detail: str = None,
        sample_size: int = None,
        scene: str = None,
        status: str = None,
        store_path: str = None,
        store_type: str = None,
        support_recall: str = None,
        user_id: int = None,
        version: int = None,
    ):
        # Classification type, binary or multi-class.
        self.classification_type = classification_type
        # Criterion value for sample data calculation
        self.data_distributed = data_distributed
        # First row of sample data. Used to define the values of each column.
        self.data_title = data_title
        # Deletion tag.
        self.delete_tag = delete_tag
        # Description information.
        self.description = description
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Primary key ID
        self.id = id
        # Name
        self.name = name
        # Number of normal samples
        self.normal_size = normal_size
        # Recall configuration
        self.recall_config = recall_config
        # Number of risk samples
        self.risk_size = risk_size
        # Specified risk value
        self.risk_value = risk_value
        # Sample label details
        self.sample_label_detail = sample_label_detail
        # Sample size
        self.sample_size = sample_size
        # Scene code
        self.scene = scene
        # Status.
        self.status = status
        # Storage path
        self.store_path = store_path
        # Storage type
        self.store_type = store_type
        # Whether recall is supported
        self.support_recall = support_recall
        # User UID
        self.user_id = user_id
        # Version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classification_type is not None:
            result['classificationType'] = self.classification_type

        if self.data_distributed is not None:
            result['dataDistributed'] = self.data_distributed

        if self.data_title is not None:
            result['dataTitle'] = self.data_title

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.normal_size is not None:
            result['normalSize'] = self.normal_size

        if self.recall_config is not None:
            result['recallConfig'] = self.recall_config

        if self.risk_size is not None:
            result['riskSize'] = self.risk_size

        if self.risk_value is not None:
            result['riskValue'] = self.risk_value

        if self.sample_label_detail is not None:
            result['sampleLabelDetail'] = self.sample_label_detail

        if self.sample_size is not None:
            result['sampleSize'] = self.sample_size

        if self.scene is not None:
            result['scene'] = self.scene

        if self.status is not None:
            result['status'] = self.status

        if self.store_path is not None:
            result['storePath'] = self.store_path

        if self.store_type is not None:
            result['storeType'] = self.store_type

        if self.support_recall is not None:
            result['supportRecall'] = self.support_recall

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classificationType') is not None:
            self.classification_type = m.get('classificationType')

        if m.get('dataDistributed') is not None:
            self.data_distributed = m.get('dataDistributed')

        if m.get('dataTitle') is not None:
            self.data_title = m.get('dataTitle')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('normalSize') is not None:
            self.normal_size = m.get('normalSize')

        if m.get('recallConfig') is not None:
            self.recall_config = m.get('recallConfig')

        if m.get('riskSize') is not None:
            self.risk_size = m.get('riskSize')

        if m.get('riskValue') is not None:
            self.risk_value = m.get('riskValue')

        if m.get('sampleLabelDetail') is not None:
            self.sample_label_detail = m.get('sampleLabelDetail')

        if m.get('sampleSize') is not None:
            self.sample_size = m.get('sampleSize')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('storePath') is not None:
            self.store_path = m.get('storePath')

        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')

        if m.get('supportRecall') is not None:
            self.support_recall = m.get('supportRecall')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

