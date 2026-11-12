# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListPlansResponseBody(DaraModel):
    def __init__(
        self,
        plans: List[main_models.ListPlansResponseBodyPlans] = None,
        request_id: str = None,
    ):
        # The plan information.
        self.plans = plans
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.plans:
            for v1 in self.plans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Plans'] = []
        if self.plans is not None:
            for k1 in self.plans:
                result['Plans'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plans = []
        if m.get('Plans') is not None:
            for k1 in m.get('Plans'):
                temp_model = main_models.ListPlansResponseBodyPlans()
                self.plans.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPlansResponseBodyPlans(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        core: int = None,
        credits: int = None,
        currency: str = None,
        disk_size: int = None,
        disk_type: str = None,
        flow: int = None,
        isp_type: str = None,
        memory: float = None,
        origin_price: str = None,
        plan_id: str = None,
        plan_type: str = None,
        public_ip_num: str = None,
        support_platform: str = None,
        tags: List[main_models.ListPlansResponseBodyPlansTags] = None,
        tokens: int = None,
    ):
        # The peak bandwidth. Unit: Mbps.
        self.bandwidth = bandwidth
        # The number of vCPUs.
        self.core = core
        # The number of credits.
        self.credits = credits
        # The currency unit. Valid values:
        # 
        # - CNY: Chinese Yuan.
        # 
        # - USD: US Dollar.
        # 
        # > The currency unit is CNY on the China site and USD on the international site.
        self.currency = currency
        # The disk capacity. Unit: GiB.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # - ESSD: Enterprise SSD (ESSD) at performance level (PL) 0.
        # - SSD: standard SSD.
        # - CLOUD_EFFICIENCY: ultra cloud disk.
        self.disk_type = disk_type
        # The monthly data transfer quota. Unit: GB.
        self.flow = flow
        # The public network line type. Valid values:
        # - **BGP** (default): BGP line.
        # - **BGP_NCO**: BGP (outside the Chinese mainland optimized) line.
        self.isp_type = isp_type
        # The memory size. Unit: GiB.
        self.memory = memory
        # The monthly price of the simple application server plan.
        self.origin_price = origin_price
        # The plan ID.
        self.plan_id = plan_id
        # The plan type. Valid values:
        # 
        # - NORMAL: general-purpose.
        # - CAPACITY: storage-optimized.
        # - PREVIOUS: previous generation.
        # - MULTI_IP: multiple public IP addresses.
        # - INTERNATIONAL: international.
        # 
        # > For more information, see [Instance families](https://help.aliyun.com/document_detail/2861773.html).
        self.plan_type = plan_type
        # The number of public IP addresses.
        self.public_ip_num = public_ip_num
        # The operating system type supported by the plan.
        self.support_platform = support_platform
        # The tags.
        self.tags = tags
        # The number of tokens.
        self.tokens = tokens

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.core is not None:
            result['Core'] = self.core

        if self.credits is not None:
            result['Credits'] = self.credits

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.flow is not None:
            result['Flow'] = self.flow

        if self.isp_type is not None:
            result['IspType'] = self.isp_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.public_ip_num is not None:
            result['PublicIpNum'] = self.public_ip_num

        if self.support_platform is not None:
            result['SupportPlatform'] = self.support_platform

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tokens is not None:
            result['Tokens'] = self.tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('Credits') is not None:
            self.credits = m.get('Credits')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('PublicIpNum') is not None:
            self.public_ip_num = m.get('PublicIpNum')

        if m.get('SupportPlatform') is not None:
            self.support_platform = m.get('SupportPlatform')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPlansResponseBodyPlansTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')

        return self

class ListPlansResponseBodyPlansTags(DaraModel):
    def __init__(
        self,
        cn_title: str = None,
        color: str = None,
        en_title: str = None,
    ):
        # The Chinese title.
        self.cn_title = cn_title
        # The color.
        self.color = color
        # The English title.
        self.en_title = en_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_title is not None:
            result['CnTitle'] = self.cn_title

        if self.color is not None:
            result['Color'] = self.color

        if self.en_title is not None:
            result['EnTitle'] = self.en_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnTitle') is not None:
            self.cn_title = m.get('CnTitle')

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('EnTitle') is not None:
            self.en_title = m.get('EnTitle')

        return self

