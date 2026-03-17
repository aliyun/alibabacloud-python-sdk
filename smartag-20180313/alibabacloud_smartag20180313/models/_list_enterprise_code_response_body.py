# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ListEnterpriseCodeResponseBody(DaraModel):
    def __init__(
        self,
        enterprise_codes: List[main_models.ListEnterpriseCodeResponseBodyEnterpriseCodes] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about enterprise codes.
        self.enterprise_codes = enterprise_codes
        # The number of entries returned per page.
        self.max_results = max_results
        # The token for returning the next page when the data is returned in more than one page.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.enterprise_codes:
            for v1 in self.enterprise_codes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnterpriseCodes'] = []
        if self.enterprise_codes is not None:
            for k1 in self.enterprise_codes:
                result['EnterpriseCodes'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.enterprise_codes = []
        if m.get('EnterpriseCodes') is not None:
            for k1 in m.get('EnterpriseCodes'):
                temp_model = main_models.ListEnterpriseCodeResponseBodyEnterpriseCodes()
                self.enterprise_codes.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEnterpriseCodeResponseBodyEnterpriseCodes(DaraModel):
    def __init__(
        self,
        enterprise_code: str = None,
        is_default: bool = None,
    ):
        # The enterprise code.
        self.enterprise_code = enterprise_code
        # Indicates whether the enterprise code is the default one.
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_code is not None:
            result['EnterpriseCode'] = self.enterprise_code

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseCode') is not None:
            self.enterprise_code = m.get('EnterpriseCode')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        return self

