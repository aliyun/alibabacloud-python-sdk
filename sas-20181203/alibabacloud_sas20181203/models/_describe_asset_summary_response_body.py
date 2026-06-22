# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetSummaryResponseBody(DaraModel):
    def __init__(
        self,
        assets_summary: main_models.DescribeAssetSummaryResponseBodyAssetsSummary = None,
        request_id: str = None,
    ):
        # The asset statistics information.
        self.assets_summary = assets_summary
        # The ID of the request. The ID is a unique identifier that Alibaba Cloud generates for the request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.assets_summary:
            self.assets_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_summary is not None:
            result['AssetsSummary'] = self.assets_summary.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsSummary') is not None:
            temp_model = main_models.DescribeAssetSummaryResponseBodyAssetsSummary()
            self.assets_summary = temp_model.from_map(m.get('AssetsSummary'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAssetSummaryResponseBodyAssetsSummary(DaraModel):
    def __init__(
        self,
        total_asset_all_region: int = None,
        total_core_all_region: int = None,
        total_core_num: int = None,
    ):
        # The total number of assets across all regions.
        # >Security Center uses independent service centers in the Chinese mainland and outside the Chinese mainland. You can check the endpoint to which you are connected to determine the current service region. For more information about the regions included in each service region, see [What is Security Center?](https://help.aliyun.com/document_detail/42302.html).
        self.total_asset_all_region = total_asset_all_region
        # The total number of cores of assets across all regions.
        # >Security Center uses independent service centers in the Chinese mainland and outside the Chinese mainland. You can check the endpoint to which you are connected to determine the current service region. For more information about the regions included in each service region, see [What is Security Center?](https://help.aliyun.com/document_detail/42302.html).
        self.total_core_all_region = total_core_all_region
        # The total number of cores of assets in the current region.
        # 
        # >Security Center uses independent service centers in the Chinese mainland and outside the Chinese mainland. You can check the endpoint to which you are connected to determine the current service region. For more information about the regions included in each service region, see [What is Security Center?](https://help.aliyun.com/document_detail/42302.html).
        self.total_core_num = total_core_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_asset_all_region is not None:
            result['TotalAssetAllRegion'] = self.total_asset_all_region

        if self.total_core_all_region is not None:
            result['TotalCoreAllRegion'] = self.total_core_all_region

        if self.total_core_num is not None:
            result['TotalCoreNum'] = self.total_core_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalAssetAllRegion') is not None:
            self.total_asset_all_region = m.get('TotalAssetAllRegion')

        if m.get('TotalCoreAllRegion') is not None:
            self.total_core_all_region = m.get('TotalCoreAllRegion')

        if m.get('TotalCoreNum') is not None:
            self.total_core_num = m.get('TotalCoreNum')

        return self

