# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCloudAssetSummaryResponseBody(DaraModel):
    def __init__(
        self,
        grouped_fields: main_models.GetCloudAssetSummaryResponseBodyGroupedFields = None,
        request_id: str = None,
    ):
        # Summary information of cloud assets.
        self.grouped_fields = grouped_fields
        # 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。
        self.request_id = request_id

    def validate(self):
        if self.grouped_fields:
            self.grouped_fields.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grouped_fields is not None:
            result['GroupedFields'] = self.grouped_fields.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupedFields') is not None:
            temp_model = main_models.GetCloudAssetSummaryResponseBodyGroupedFields()
            self.grouped_fields = temp_model.from_map(m.get('GroupedFields'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCloudAssetSummaryResponseBodyGroupedFields(DaraModel):
    def __init__(
        self,
        cloud_asset_summary_metas: List[main_models.GetCloudAssetSummaryResponseBodyGroupedFieldsCloudAssetSummaryMetas] = None,
        instance_count_total: int = None,
        instance_risk_count_total: int = None,
    ):
        # List of cloud product statistics
        self.cloud_asset_summary_metas = cloud_asset_summary_metas
        # Total number of cloud product instances.
        self.instance_count_total = instance_count_total
        # Total number of cloud product instances at risk
        self.instance_risk_count_total = instance_risk_count_total

    def validate(self):
        if self.cloud_asset_summary_metas:
            for v1 in self.cloud_asset_summary_metas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudAssetSummaryMetas'] = []
        if self.cloud_asset_summary_metas is not None:
            for k1 in self.cloud_asset_summary_metas:
                result['CloudAssetSummaryMetas'].append(k1.to_map() if k1 else None)

        if self.instance_count_total is not None:
            result['InstanceCountTotal'] = self.instance_count_total

        if self.instance_risk_count_total is not None:
            result['InstanceRiskCountTotal'] = self.instance_risk_count_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_asset_summary_metas = []
        if m.get('CloudAssetSummaryMetas') is not None:
            for k1 in m.get('CloudAssetSummaryMetas'):
                temp_model = main_models.GetCloudAssetSummaryResponseBodyGroupedFieldsCloudAssetSummaryMetas()
                self.cloud_asset_summary_metas.append(temp_model.from_map(k1))

        if m.get('InstanceCountTotal') is not None:
            self.instance_count_total = m.get('InstanceCountTotal')

        if m.get('InstanceRiskCountTotal') is not None:
            self.instance_risk_count_total = m.get('InstanceRiskCountTotal')

        return self

class GetCloudAssetSummaryResponseBodyGroupedFieldsCloudAssetSummaryMetas(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        instance_count: int = None,
        instance_risk_count: int = None,
        vendor: int = None,
    ):
        # Subtype of the cloud product
        self.asset_sub_type = asset_sub_type
        # 云产品的类型。取值：
        # 
        # - **0**：云服务器 ECS
        # - **1**：负载均衡
        # - **3**：云数据库 RDS
        # - **4**：云数据库 MongoDB 版
        # - **5**：云数据库 Tair（兼容 Redis）
        # - **6**：容器镜像服务
        # - **8**：容器服务Kubernetes版
        # - **9**：专有网络VPC
        # - **11**：操作审计
        # - **12**：CDN
        # - **13**：数字证书管理服务（原SSL证书）
        # - **14**：云效
        # - **15**：访问控制
        # - **16**：DDoS防护
        # - **17**：Web应用防火墙
        # - **18**：对象存储
        # - **19**：云原生关系型数据库 PolarDB
        # - **20**：云数据库 PostgreSQL 版
        # - **21**：微服务引擎
        # - **22**：文件存储NAS
        # - **23**：数据安全中心
        # - **24**：弹性公网IP
        # - **25**：云身份服务-EIAM
        # - **26**：PolarDB-X
        # - **27**：Elasticsearch
        self.asset_type = asset_type
        # Total number of this type of cloud product instances.
        self.instance_count = instance_count
        # Total number of risky instances for this type of cloud product.
        self.instance_risk_count = instance_risk_count
        # 服务器厂商。取值：
        # 
        # - **0**：阿里云资产
        # - **1**：云外资产
        # - **2**：IDC资产
        # - **3**、**4**、**5**、**7**：其它云资产
        # - **8**：轻量级资产
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_risk_count is not None:
            result['InstanceRiskCount'] = self.instance_risk_count

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceRiskCount') is not None:
            self.instance_risk_count = m.get('InstanceRiskCount')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

