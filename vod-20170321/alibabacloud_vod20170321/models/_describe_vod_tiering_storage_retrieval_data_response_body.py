# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodTieringStorageRetrievalDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        retrieval_data: List[main_models.DescribeVodTieringStorageRetrievalDataResponseBodyRetrievalData] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The data retrieval information.
        self.retrieval_data = retrieval_data

    def validate(self):
        if self.retrieval_data:
            for v1 in self.retrieval_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RetrievalData'] = []
        if self.retrieval_data is not None:
            for k1 in self.retrieval_data:
                result['RetrievalData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.retrieval_data = []
        if m.get('RetrievalData') is not None:
            for k1 in m.get('RetrievalData'):
                temp_model = main_models.DescribeVodTieringStorageRetrievalDataResponseBodyRetrievalData()
                self.retrieval_data.append(temp_model.from_map(k1))

        return self

class DescribeVodTieringStorageRetrievalDataResponseBodyRetrievalData(DaraModel):
    def __init__(
        self,
        cabulk_retrieval_data: int = None,
        cahigh_prior_retrieval_data: int = None,
        castd_retrieval_data: int = None,
        region: str = None,
        retrieval_data: int = None,
        storage_class: str = None,
        time_stamp: str = None,
    ):
        # The retrieved Cold Archive data in the bulk mode.
        self.cabulk_retrieval_data = cabulk_retrieval_data
        # The retrieved Cold Archive data in the expedited mode.
        self.cahigh_prior_retrieval_data = cahigh_prior_retrieval_data
        # The retrieved Cold Archive data in the standard mode.
        self.castd_retrieval_data = castd_retrieval_data
        # The storage region.
        self.region = region
        # The data retrieval information.
        self.retrieval_data = retrieval_data
        # The storage type.
        self.storage_class = storage_class
        # The timestamp of the returned data. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabulk_retrieval_data is not None:
            result['CABulkRetrievalData'] = self.cabulk_retrieval_data

        if self.cahigh_prior_retrieval_data is not None:
            result['CAHighPriorRetrievalData'] = self.cahigh_prior_retrieval_data

        if self.castd_retrieval_data is not None:
            result['CAStdRetrievalData'] = self.castd_retrieval_data

        if self.region is not None:
            result['Region'] = self.region

        if self.retrieval_data is not None:
            result['RetrievalData'] = self.retrieval_data

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CABulkRetrievalData') is not None:
            self.cabulk_retrieval_data = m.get('CABulkRetrievalData')

        if m.get('CAHighPriorRetrievalData') is not None:
            self.cahigh_prior_retrieval_data = m.get('CAHighPriorRetrievalData')

        if m.get('CAStdRetrievalData') is not None:
            self.castd_retrieval_data = m.get('CAStdRetrievalData')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RetrievalData') is not None:
            self.retrieval_data = m.get('RetrievalData')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

