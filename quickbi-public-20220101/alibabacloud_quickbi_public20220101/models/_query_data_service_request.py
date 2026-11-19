# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDataServiceRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        conditions: str = None,
        return_fields: str = None,
    ):
        # The ID of the API in Data Service. For more information, see [Data Service](https://help.aliyun.com/document_detail/144980.html).
        # 
        # This parameter is required.
        self.api_id = api_id
        # The query conditions for Data Service, which are passed as key-value pairs. The value is a string of the map type. The key is the name of the request parameter, and the value is the value of the request parameter. Keys and values must appear in pairs.
        # 
        # **Note:**
        # 
        # - When the operator of a request parameter is set to **Enum Filter**, the value can contain multiple values. In this case, the value must be a JSON-formatted list. Example: `area=["East China","North China","South China"]`     
        # 
        # - For dates, different input formats are provided based on the type:
        # 
        #     - Year: 2019
        # 
        #     - Quarter: 2019Q1
        # 
        #     - Month: 201901 (including the leading zero)
        #     
        #     - Week: 2019-52
        # 
        #     - Day: 20190101
        # 
        #     - Hour: 14:00:00 (minutes and seconds are 00)
        #     
        #     - Minute: 14:12:00 (seconds are 00)
        # 
        #     - Second: 14:34:34
        self.conditions = conditions
        # The list of names of the response parameters. The value is a string of the list type.
        self.return_fields = return_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.conditions is not None:
            result['Conditions'] = self.conditions

        if self.return_fields is not None:
            result['ReturnFields'] = self.return_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')

        if m.get('ReturnFields') is not None:
            self.return_fields = m.get('ReturnFields')

        return self

