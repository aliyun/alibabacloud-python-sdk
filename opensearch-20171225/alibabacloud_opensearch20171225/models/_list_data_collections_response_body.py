# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListDataCollectionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListDataCollectionsResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the data collection task.
        # 
        # For more information, see [DataCollection](https://help.aliyun.com/document_detail/173605.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListDataCollectionsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListDataCollectionsResponseBodyResult(DaraModel):
    def __init__(
        self,
        created: int = None,
        data_collection_type: str = None,
        id: str = None,
        industry_name: str = None,
        name: str = None,
        status: int = None,
        sundial_id: str = None,
        type: str = None,
        updated: int = None,
    ):
        # The time when the task was created.
        self.created = created
        # The type of data collected. Valid values:
        # 
        # *   behavior: behavioral data.
        # *   item_info: project information.
        # *   industry_specific: industry-specific data.
        self.data_collection_type = data_collection_type
        # The data collection ID.
        self.id = id
        # The industry name. Valid values:
        # 
        # *   general
        # *   ecommerce
        self.industry_name = industry_name
        # The name of the data collection task.
        self.name = name
        # The status of the data collection feature. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is being enabled.
        # *   2: The feature is enabled.
        # *   3: The feature failed to be enabled.
        self.status = status
        # The sundial ID.
        self.sundial_id = sundial_id
        # The type of the source from which data was collected. Valid values:
        # 
        # *   server
        # *   web
        # *   app
        # 
        # Only server is supported.
        self.type = type
        # The time when the data collection task was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type

        if self.id is not None:
            result['id'] = self.id

        if self.industry_name is not None:
            result['industryName'] = self.industry_name

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id

        if self.type is not None:
            result['type'] = self.type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

