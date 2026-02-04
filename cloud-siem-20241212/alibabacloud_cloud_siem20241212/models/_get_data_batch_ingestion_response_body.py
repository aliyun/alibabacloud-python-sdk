# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetDataBatchIngestionResponseBody(DaraModel):
    def __init__(
        self,
        data_batch_ingestion: main_models.GetDataBatchIngestionResponseBodyDataBatchIngestion = None,
        request_id: str = None,
    ):
        self.data_batch_ingestion = data_batch_ingestion
        self.request_id = request_id

    def validate(self):
        if self.data_batch_ingestion:
            self.data_batch_ingestion.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_batch_ingestion is not None:
            result['DataBatchIngestion'] = self.data_batch_ingestion.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBatchIngestion') is not None:
            temp_model = main_models.GetDataBatchIngestionResponseBodyDataBatchIngestion()
            self.data_batch_ingestion = temp_model.from_map(m.get('DataBatchIngestion'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataBatchIngestionResponseBodyDataBatchIngestion(DaraModel):
    def __init__(
        self,
        apsara_data_ingestion_ids: List[str] = None,
        auto_scan_new: str = None,
        data_batch_ingestion_effect_time: str = None,
        data_batch_ingestion_mode: str = None,
        data_batch_ingestion_set_time: str = None,
        data_batch_ingestion_status: str = None,
        data_ingestions: List[main_models.GetDataBatchIngestionResponseBodyDataBatchIngestionDataIngestions] = None,
        data_source_recognize_enabled: bool = None,
        log_user_ids: List[str] = None,
        recommend_data_ingestion_ids: List[str] = None,
    ):
        self.apsara_data_ingestion_ids = apsara_data_ingestion_ids
        self.auto_scan_new = auto_scan_new
        self.data_batch_ingestion_effect_time = data_batch_ingestion_effect_time
        self.data_batch_ingestion_mode = data_batch_ingestion_mode
        self.data_batch_ingestion_set_time = data_batch_ingestion_set_time
        self.data_batch_ingestion_status = data_batch_ingestion_status
        self.data_ingestions = data_ingestions
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.log_user_ids = log_user_ids
        self.recommend_data_ingestion_ids = recommend_data_ingestion_ids

    def validate(self):
        if self.data_ingestions:
            for v1 in self.data_ingestions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apsara_data_ingestion_ids is not None:
            result['ApsaraDataIngestionIds'] = self.apsara_data_ingestion_ids

        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new

        if self.data_batch_ingestion_effect_time is not None:
            result['DataBatchIngestionEffectTime'] = self.data_batch_ingestion_effect_time

        if self.data_batch_ingestion_mode is not None:
            result['DataBatchIngestionMode'] = self.data_batch_ingestion_mode

        if self.data_batch_ingestion_set_time is not None:
            result['DataBatchIngestionSetTime'] = self.data_batch_ingestion_set_time

        if self.data_batch_ingestion_status is not None:
            result['DataBatchIngestionStatus'] = self.data_batch_ingestion_status

        result['DataIngestions'] = []
        if self.data_ingestions is not None:
            for k1 in self.data_ingestions:
                result['DataIngestions'].append(k1.to_map() if k1 else None)

        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled

        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids

        if self.recommend_data_ingestion_ids is not None:
            result['RecommendDataIngestionIds'] = self.recommend_data_ingestion_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsaraDataIngestionIds') is not None:
            self.apsara_data_ingestion_ids = m.get('ApsaraDataIngestionIds')

        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')

        if m.get('DataBatchIngestionEffectTime') is not None:
            self.data_batch_ingestion_effect_time = m.get('DataBatchIngestionEffectTime')

        if m.get('DataBatchIngestionMode') is not None:
            self.data_batch_ingestion_mode = m.get('DataBatchIngestionMode')

        if m.get('DataBatchIngestionSetTime') is not None:
            self.data_batch_ingestion_set_time = m.get('DataBatchIngestionSetTime')

        if m.get('DataBatchIngestionStatus') is not None:
            self.data_batch_ingestion_status = m.get('DataBatchIngestionStatus')

        self.data_ingestions = []
        if m.get('DataIngestions') is not None:
            for k1 in m.get('DataIngestions'):
                temp_model = main_models.GetDataBatchIngestionResponseBodyDataBatchIngestionDataIngestions()
                self.data_ingestions.append(temp_model.from_map(k1))

        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')

        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')

        if m.get('RecommendDataIngestionIds') is not None:
            self.recommend_data_ingestion_ids = m.get('RecommendDataIngestionIds')

        return self

class GetDataBatchIngestionResponseBodyDataBatchIngestionDataIngestions(DaraModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        data_ingestion_status: str = None,
        data_source_id: str = None,
        product_id: str = None,
        vendor_id: str = None,
    ):
        self.data_ingestion_id = data_ingestion_id
        self.data_ingestion_status = data_ingestion_status
        self.data_source_id = data_source_id
        self.product_id = product_id
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id

        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')

        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

