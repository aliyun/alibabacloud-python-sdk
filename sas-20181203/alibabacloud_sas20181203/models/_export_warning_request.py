# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportWarningRequest(DaraModel):
    def __init__(
        self,
        dealed: str = None,
        export_type: str = None,
        group_id: int = None,
        is_cleartext_pwd: int = None,
        is_summary_export: int = None,
        lang: str = None,
        risk_ids: str = None,
        risk_levels: str = None,
        risk_name: str = None,
        source_ip: str = None,
        status_list: str = None,
        strategy_id: int = None,
        sub_type_names: str = None,
        type_name: str = None,
        type_names: str = None,
        uuids: str = None,
    ):
        # Specifies whether the baseline risks are handled. Valid values:
        # 
        # *   **Y**: yes
        # *   **N**: no
        self.dealed = dealed
        # The type of the export task. Set the value to **hc_check_warning**, which indicates tasks to export baseline check results.
        self.export_type = export_type
        # The ID of the server group.
        # 
        # >  You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of server groups.
        self.group_id = group_id
        # The export method of the results for the weak password baseline check. Valid values:
        # 
        # *   **0**: exports the check results after it is masked.
        # *   **1**: exports the check results in plaintext.
        self.is_cleartext_pwd = is_cleartext_pwd
        # Specifies whether the baseline check results are aggregated and exported. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.is_summary_export = is_summary_export
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the risk item in the baseline check results. Separate multiple IDs with commas (,).
        self.risk_ids = risk_ids
        # The severity of the baseline check item. Separate multiple severities with commas (,). Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_levels = risk_levels
        # The name of the baseline.
        self.risk_name = risk_name
        # The source IP address of the request.
        self.source_ip = source_ip
        # The status of the check item in the baseline check results. Separate multiple statuses with commas (,). Valid values:
        # 
        # *   **3**: passed
        # *   **1**: failed
        self.status_list = status_list
        # The ID of the baseline check policy.
        self.strategy_id = strategy_id
        # The subtypes of the baselines based on which baseline checks are performed. Separate multiple subtypes with commas (,).
        # 
        # > You must set the value of this parameter to the value of the **TypeName** parameter that is contained in the **SubTypes** parameter. You can call the [DescribeRiskType](~~DescribeRiskType~~) operation to obtain the value of the TypeName parameter.
        self.sub_type_names = sub_type_names
        # The type of the baseline based on which baseline checks are performed.
        # 
        # > You must set the value of this parameter to the value of the **TypeName** parameter that is returned by calling the [DescribeRiskType](~~DescribeRiskType~~) operation. If both the **TypeName** and **TypeNames** parameters are specified, only the **TypeName** parameter takes effect.
        self.type_name = type_name
        # The types of the baselines based on which baseline checks are performed. Separate multiple types with commas (,).
        # 
        # > You must set the value of this parameter to the value of the **TypeName** parameter that is returned by calling the [DescribeRiskType](~~DescribeRiskType~~) operation. If both the **TypeName** and **TypeNames** parameters are specified, only the **TypeName** parameter takes effect.
        self.type_names = type_names
        # The UUID of the server whose baseline check results you want to export. Separate multiple UUIDs with commas (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.is_cleartext_pwd is not None:
            result['IsCleartextPwd'] = self.is_cleartext_pwd

        if self.is_summary_export is not None:
            result['IsSummaryExport'] = self.is_summary_export

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.risk_ids is not None:
            result['RiskIds'] = self.risk_ids

        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.sub_type_names is not None:
            result['SubTypeNames'] = self.sub_type_names

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        if self.type_names is not None:
            result['TypeNames'] = self.type_names

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IsCleartextPwd') is not None:
            self.is_cleartext_pwd = m.get('IsCleartextPwd')

        if m.get('IsSummaryExport') is not None:
            self.is_summary_export = m.get('IsSummaryExport')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RiskIds') is not None:
            self.risk_ids = m.get('RiskIds')

        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('SubTypeNames') is not None:
            self.sub_type_names = m.get('SubTypeNames')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        if m.get('TypeNames') is not None:
            self.type_names = m.get('TypeNames')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

