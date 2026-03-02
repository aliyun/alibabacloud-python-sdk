# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListAssetCountResponseBody(DaraModel):
    def __init__(
        self,
        asset_count_list: List[main_models.ListAssetCountResponseBodyAssetCountList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        self.asset_count_list = asset_count_list
        self.current_page = current_page
        self.request_id = request_id
        self.show_size = show_size
        self.total_count = total_count

    def validate(self):
        if self.asset_count_list:
            for v1 in self.asset_count_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetCountList'] = []
        if self.asset_count_list is not None:
            for k1 in self.asset_count_list:
                result['AssetCountList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_count_list = []
        if m.get('AssetCountList') is not None:
            for k1 in m.get('AssetCountList'):
                temp_model = main_models.ListAssetCountResponseBodyAssetCountList()
                self.asset_count_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAssetCountResponseBodyAssetCountList(DaraModel):
    def __init__(
        self,
        aliyun_asset_count: int = None,
        certificate_count: int = None,
        count_date: int = None,
        domain_asset_count: int = None,
        multi_cloud_asset_count: int = None,
        points: int = None,
    ):
        self.aliyun_asset_count = aliyun_asset_count
        self.certificate_count = certificate_count
        self.count_date = count_date
        self.domain_asset_count = domain_asset_count
        self.multi_cloud_asset_count = multi_cloud_asset_count
        self.points = points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_asset_count is not None:
            result['AliyunAssetCount'] = self.aliyun_asset_count

        if self.certificate_count is not None:
            result['CertificateCount'] = self.certificate_count

        if self.count_date is not None:
            result['CountDate'] = self.count_date

        if self.domain_asset_count is not None:
            result['DomainAssetCount'] = self.domain_asset_count

        if self.multi_cloud_asset_count is not None:
            result['MultiCloudAssetCount'] = self.multi_cloud_asset_count

        if self.points is not None:
            result['Points'] = self.points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunAssetCount') is not None:
            self.aliyun_asset_count = m.get('AliyunAssetCount')

        if m.get('CertificateCount') is not None:
            self.certificate_count = m.get('CertificateCount')

        if m.get('CountDate') is not None:
            self.count_date = m.get('CountDate')

        if m.get('DomainAssetCount') is not None:
            self.domain_asset_count = m.get('DomainAssetCount')

        if m.get('MultiCloudAssetCount') is not None:
            self.multi_cloud_asset_count = m.get('MultiCloudAssetCount')

        if m.get('Points') is not None:
            self.points = m.get('Points')

        return self

