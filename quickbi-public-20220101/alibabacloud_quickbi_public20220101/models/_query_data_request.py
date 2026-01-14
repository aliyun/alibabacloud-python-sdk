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
        # The API ID in the data service. For more information, see: [Data Service](https://help.aliyun.com/document_detail/144980.html).
        # 
        # This parameter is required.
        self.api_id = api_id
        # The query conditions for the data service, passed in as Key and Value pairs. A map-type string. Here, Key is the name of the request parameter, and Value is the value of the request parameter. Key and Value must appear in pairs.
        # 
        # **Note:**
        # 
        # - When the operator of the request parameter is set to **enumeration filtering**, the value can contain multiple values, and the format of the value should be a JSON-formatted List. For example: `area=["East China","North China","South China"]`
        # 
        # - For dates, different formats are provided based on the type:
        # 
        #     - Year: 2019
        # 
        #     - Quarter: 2019Q1
        # 
        #     - Month: 201901 (with leading zero)
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
        # A list of return parameter names, in a List-type string.
        self.return_fields = return_fields
        # The userId in Quick BI. For how to obtain the userId, see: [Query User Information by Account Interface](https://next.api.aliyun.com/document/quickbi-public/2022-01-01/QueryUserInfoByAccount)
        # > This parameter is used to specify the identity of the person using the data service, which can be used in conjunction with the row and column permission configurations of the dataset.
        # 
        # 
        # 
        # >Notice: If the parameter is not passed, an empty string is passed, or null is passed, the default userId will be the owner of the current Quick BI organization.</notice>
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

