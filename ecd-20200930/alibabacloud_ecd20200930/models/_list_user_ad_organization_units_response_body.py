# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ListUserAdOrganizationUnitsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        ounames: List[main_models.ListUserAdOrganizationUnitsResponseBodyOUNames] = None,
        request_id: str = None,
    ):
        # A pagination token.
        self.next_token = next_token
        # The OUs of the AD domain.
        self.ounames = ounames
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ounames:
            for v1 in self.ounames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['OUNames'] = []
        if self.ounames is not None:
            for k1 in self.ounames:
                result['OUNames'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.ounames = []
        if m.get('OUNames') is not None:
            for k1 in m.get('OUNames'):
                temp_model = main_models.ListUserAdOrganizationUnitsResponseBodyOUNames()
                self.ounames.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUserAdOrganizationUnitsResponseBodyOUNames(DaraModel):
    def __init__(
        self,
        display_ouname: str = None,
        ouname: str = None,
        office_site_id: str = None,
    ):
        # The name of the OU.
        self.display_ouname = display_ouname
        # The canonical name (CNAME) of the OU in the AD domain controller.
        self.ouname = ouname
        # The enterprise AD office network ID.
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_ouname is not None:
            result['DisplayOUName'] = self.display_ouname

        if self.ouname is not None:
            result['OUName'] = self.ouname

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayOUName') is not None:
            self.display_ouname = m.get('DisplayOUName')

        if m.get('OUName') is not None:
            self.ouname = m.get('OUName')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        return self

