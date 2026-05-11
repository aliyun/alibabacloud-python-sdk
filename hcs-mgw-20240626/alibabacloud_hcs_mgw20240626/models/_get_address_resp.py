# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class GetAddressResp(DaraModel):
    def __init__(
        self,
        address_detail: main_models.AddressDetail = None,
        create_time: str = None,
        modify_time: str = None,
        name: str = None,
        owner: str = None,
        status: str = None,
        tags: str = None,
        verify_result: main_models.VerifyResp = None,
        verify_time: str = None,
        version: str = None,
    ):
        # The details of the data address.
        self.address_detail = address_detail
        # The time when the data address was created.
        self.create_time = create_time
        # The time when the data address was last modified.
        self.modify_time = modify_time
        # The name of the data address.
        self.name = name
        # The owner of the data address.
        self.owner = owner
        # The state of the data address.
        self.status = status
        # The tags.
        self.tags = tags
        # The verification result of the data address.
        self.verify_result = verify_result
        # The time when the data address was verified.
        self.verify_time = verify_time
        # The ID of the data address.
        self.version = version

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()
        if self.verify_result:
            self.verify_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result.to_map()

        if self.verify_time is not None:
            result['VerifyTime'] = self.verify_time

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            temp_model = main_models.AddressDetail()
            self.address_detail = temp_model.from_map(m.get('AddressDetail'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('VerifyResult') is not None:
            temp_model = main_models.VerifyResp()
            self.verify_result = temp_model.from_map(m.get('VerifyResult'))

        if m.get('VerifyTime') is not None:
            self.verify_time = m.get('VerifyTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

