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
        # The statistical information about the assets.
        self.assets_summary = assets_summary
        # The ID of the request, which is used to locate and troubleshoot issues.
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
        # The total number of protected assets in all regions.
        # 
        # >  Security Center supports the Hangzhou and Singapore service centers, which separately correspond to the China and Outside China data management centers. In the Hangzhou service center, Security Center provides protection capabilities for assets that are deployed in the regions covered by the China data management center. In the Singapore service center, Security Center provides protection capabilities for assets that are deployed in the regions covered by the Outside China data management center. You can determine whether the current region is covered by the China data management center or by the Outside China data management center based on the endpoint of Security Center. For more information about the supported regions for each data management center, see [What is Security Center?](https://help.aliyun.com/document_detail/42302.html)
        self.total_asset_all_region = total_asset_all_region
        # The total number of cores of protected assets in all regions.
        # 
        # >  Security Center supports the Hangzhou and Singapore service centers, which separately correspond to the China and Outside China data management centers. In the Hangzhou service center, Security Center provides protection capabilities for assets that are deployed in the regions covered by the China data management center. In the Singapore service center, Security Center provides protection capabilities for assets that are deployed in the regions covered by the Outside China data management center. You can determine whether the current region is covered by the China data management center or by the Outside China data management center based on the endpoint of Security Center. For more information about the supported regions for each data management center, see [What is Security Center?](https://help.aliyun.com/document_detail/42302.html)
        self.total_core_all_region = total_core_all_region
        # The total number of cores of protected assets in the current region.
        # 
        # >  Security Center supports the Hangzhou and Singapore service centers, which separately correspond to the China and Outside China data management centers. In the Hangzhou service center, Security Center provides protection capabilities for assets that are deployed in the regions covered by the China data management center. In the Singapore service center, Security Center provides protection capabilities for assets that are deployed in the regions covered by the Outside China data management center. You can determine whether the current region is covered by the China data management center or by the Outside China data management center based on the endpoint of Security Center. For more information about the supported regions for each data management center, see [What is Security Center?](https://help.aliyun.com/document_detail/42302.html)
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

