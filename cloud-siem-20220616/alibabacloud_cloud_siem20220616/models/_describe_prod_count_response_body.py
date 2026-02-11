# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeProdCountResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeProdCountResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeProdCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeProdCountResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_imported_count: int = None,
        aliyun_prod_count: int = None,
        hcloud_imported_count: int = None,
        hcloud_prod_count: int = None,
        idc_imported_count: int = None,
        idc_prod_count: int = None,
        qcloud_imported_count: int = None,
        qcloud_prod_count: int = None,
    ):
        self.aliyun_imported_count = aliyun_imported_count
        # The number of Alibaba Cloud services.
        self.aliyun_prod_count = aliyun_prod_count
        self.hcloud_imported_count = hcloud_imported_count
        # The number of Huawei Cloud services.
        self.hcloud_prod_count = hcloud_prod_count
        self.idc_imported_count = idc_imported_count
        self.idc_prod_count = idc_prod_count
        self.qcloud_imported_count = qcloud_imported_count
        # The number of Tencent Cloud services.
        self.qcloud_prod_count = qcloud_prod_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_imported_count is not None:
            result['AliyunImportedCount'] = self.aliyun_imported_count

        if self.aliyun_prod_count is not None:
            result['AliyunProdCount'] = self.aliyun_prod_count

        if self.hcloud_imported_count is not None:
            result['HcloudImportedCount'] = self.hcloud_imported_count

        if self.hcloud_prod_count is not None:
            result['HcloudProdCount'] = self.hcloud_prod_count

        if self.idc_imported_count is not None:
            result['IdcImportedCount'] = self.idc_imported_count

        if self.idc_prod_count is not None:
            result['IdcProdCount'] = self.idc_prod_count

        if self.qcloud_imported_count is not None:
            result['QcloudImportedCount'] = self.qcloud_imported_count

        if self.qcloud_prod_count is not None:
            result['QcloudProdCount'] = self.qcloud_prod_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunImportedCount') is not None:
            self.aliyun_imported_count = m.get('AliyunImportedCount')

        if m.get('AliyunProdCount') is not None:
            self.aliyun_prod_count = m.get('AliyunProdCount')

        if m.get('HcloudImportedCount') is not None:
            self.hcloud_imported_count = m.get('HcloudImportedCount')

        if m.get('HcloudProdCount') is not None:
            self.hcloud_prod_count = m.get('HcloudProdCount')

        if m.get('IdcImportedCount') is not None:
            self.idc_imported_count = m.get('IdcImportedCount')

        if m.get('IdcProdCount') is not None:
            self.idc_prod_count = m.get('IdcProdCount')

        if m.get('QcloudImportedCount') is not None:
            self.qcloud_imported_count = m.get('QcloudImportedCount')

        if m.get('QcloudProdCount') is not None:
            self.qcloud_prod_count = m.get('QcloudProdCount')

        return self

