# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDataRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        conditions: str = None,
        return_fields: str = None,
        user_id: str = None,
    ):
        # The API ID in [DataService Studio](https://help.aliyun.com/document_detail/144980.html).
        # 
        # This parameter is required.
        self.api_id = api_id
        # Filter conditions as a JSON map string. Each key is a request parameter name, and each value is the parameter value.
        # 
        # **Note:**
        # 
        # - If the operator of a request parameter is set to **Enumeration Filter**, the value can contain multiple values. In this case, the value must be in the format of a JSON list. For example: `area=["East China","North China","South China"]`
        # 
        # - For dates, use the following formats based on the date type:
        # 
        #   - Year: 2019
        # 
        #   - Quarter: 2019Q1
        # 
        #   - Month: 201901 (with a leading zero)
        # 
        #   - Week: 2019-52
        # 
        #   - Day: 20190101
        # 
        #   - Hour: 14:00:00 (minutes and seconds are 00)
        # 
        #   - Minute: 14:12:00 (seconds are 00)
        # 
        #   - Second: 14:34:34
        self.conditions = conditions
        # A JSON array of field names to return.
        self.return_fields = return_fields
        # The Quick BI user ID. Obtain this value from [QueryUserInfoByAccount](https://next.api.aliyun.com/document/quickbi-public/2022-01-01/QueryUserInfoByAccount).
        # 
        # > Specifies the user identity for DataService Studio, used with row-level and column-level permission configurations.
        # 
        # >Notice: 
        # 
        # If omitted, empty, or null, defaults to the Quick BI organization owner\\"s user ID.
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')

        if m.get('ReturnFields') is not None:
            self.return_fields = m.get('ReturnFields')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

