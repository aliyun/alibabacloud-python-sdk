# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreviewGtmRecoveryPlanRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        recovery_plan_id: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # zh: Chinese
        # 
        # en: English
        # 
        # Default: en
        self.lang = lang
        # The page number. The value starts from **1**. Default: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **20**. Default: **5**.
        self.page_size = page_size
        # The ID of the disaster recovery plan.<props="china">You can call the [DescribeGtmRecoveryPlans](https://help.aliyun.com/zh/dns/api-alidns-2015-01-09-describegtmrecoveryplans?spm=a2c4g.11186623.help-menu-29697.d_0_5_1_3_13_5.6dd83618vW4yD7) operation to obtain the ID.<props="intl">You can call the [DescribeGtmRecoveryPlans](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describegtmrecoveryplans?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the ID.
        # 
        # This parameter is required.
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')

        return self

