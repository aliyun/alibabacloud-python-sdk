# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BindAuthToMachineRequest(DaraModel):
    def __init__(
        self,
        auth_version: int = None,
        auto_bind: int = None,
        bind: List[str] = None,
        bind_all: bool = None,
        criteria: str = None,
        is_pre_bind: int = None,
        logical_exp: str = None,
        ntm_version: str = None,
        pre_bind_order_id: int = None,
        un_bind: List[str] = None,
    ):
        # The edition of Security Center that is authorized to scan the asset. Valid values:
        # 
        # *   **6**: Anti-virus
        # *   **5**: Advanced
        # *   **3**: Enterprise
        # *   **7**: Ultimate
        # *   **10**: Value-added Plan
        self.auth_version = auth_version
        # Specifies whether to automatically bind servers to Security Center. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.auto_bind = auto_bind
        # The UUIDs of the servers that you want to bind to Security Center.
        # 
        # >  You must specify at least one of the **Bind** and **UnBind** parameters.
        self.bind = bind
        # Specifies whether to bind all servers to Security Center. Default value: **false**. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.bind_all = bind_all
        # The search conditions that are used to filter servers. The value of this parameter is in the JSON format and is case-sensitive.
        # 
        # >  A search condition can be an instance ID, instance name, virtual private cloud (VPC) ID, region, or public IP address. You can call the [DescribeCriteria](~~DescribeCriteria~~) operation to query the supported search conditions.
        self.criteria = criteria
        # Specifies whether to specify servers for protection when you purchase Security Center. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # >  If you specify servers, the servers are automatically added to Security Center for protection after the purchase order is complete.
        self.is_pre_bind = is_pre_bind
        # The logical relationship that you want to use to evaluate multiple search conditions. Default value: **OR**. Valid values:
        # 
        # *   **OR**
        # *   **AND**
        self.logical_exp = logical_exp
        # The edition of Security Center that you purchase in the order. Valid values:
        # 
        # *   **level7**: Anti-virus
        # *   **level3**: Advanced
        # *   **level2**: Enterprise
        # *   **level8**: Ultimate
        # *   **level10**: Value-added Plan
        self.ntm_version = ntm_version
        # The ID of the order in which Security Center is purchased and servers are specified for protection.
        self.pre_bind_order_id = pre_bind_order_id
        # The UUIDs of the servers that you want to unbind from Security Center.
        # 
        # >  You must specify at least one of the **Bind** and **UnBind** parameters.
        self.un_bind = un_bind

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        if self.bind is not None:
            result['Bind'] = self.bind

        if self.bind_all is not None:
            result['BindAll'] = self.bind_all

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.is_pre_bind is not None:
            result['IsPreBind'] = self.is_pre_bind

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.ntm_version is not None:
            result['NtmVersion'] = self.ntm_version

        if self.pre_bind_order_id is not None:
            result['PreBindOrderId'] = self.pre_bind_order_id

        if self.un_bind is not None:
            result['UnBind'] = self.un_bind

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('BindAll') is not None:
            self.bind_all = m.get('BindAll')

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('IsPreBind') is not None:
            self.is_pre_bind = m.get('IsPreBind')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('NtmVersion') is not None:
            self.ntm_version = m.get('NtmVersion')

        if m.get('PreBindOrderId') is not None:
            self.pre_bind_order_id = m.get('PreBindOrderId')

        if m.get('UnBind') is not None:
            self.un_bind = m.get('UnBind')

        return self

