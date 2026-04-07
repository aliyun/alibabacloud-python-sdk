# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOpRiskDataRequest(DaraModel):
    def __init__(
        self,
        date: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        risk_type: str = None,
    ):
        # The date on which access records were generated. Specify the value in the yyyyMMdd format.
        # 
        # This parameter is required.
        self.date = date
        # The parameters that you can configure to query the access records. Valid values:
        # 
        # *   dbType
        # *   instanceName
        # *   databaseName
        # *   projectName
        # *   clusterName
        # 
        # The following example shows the parameters configured to query the access records of the sensitive data in the abc database of the Hologres instance ABC: [ {"dbType":"hologres","instanceName":"ABC","databaseName":"abc"} ]
        # 
        # You must configure the parameters based on the compute engine that you use in your business.
        self.name = name
        # The page number. Pages start from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The method that you use to identify risks.
        # 
        # *   You can manually identify risks.
        # *   You can also use a sensitive data identification rule to identify risks. You can log on to the DataWorks console and go to the Risk Identification Rules page in Data Security Guard to obtain the name of the rule.
        self.risk_type = risk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        return self

