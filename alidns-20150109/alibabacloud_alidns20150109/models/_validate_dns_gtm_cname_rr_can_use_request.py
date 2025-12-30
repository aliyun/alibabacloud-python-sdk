# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateDnsGtmCnameRrCanUseRequest(DaraModel):
    def __init__(
        self,
        cname_mode: str = None,
        cname_rr: str = None,
        cname_type: str = None,
        cname_zone: str = None,
        instance_id: str = None,
        lang: str = None,
    ):
        # This parameter is required.
        self.cname_mode = cname_mode
        # This parameter is required.
        self.cname_rr = cname_rr
        # This parameter is required.
        self.cname_type = cname_type
        # This parameter is required.
        self.cname_zone = cname_zone
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname_mode is not None:
            result['CnameMode'] = self.cname_mode

        if self.cname_rr is not None:
            result['CnameRr'] = self.cname_rr

        if self.cname_type is not None:
            result['CnameType'] = self.cname_type

        if self.cname_zone is not None:
            result['CnameZone'] = self.cname_zone

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnameMode') is not None:
            self.cname_mode = m.get('CnameMode')

        if m.get('CnameRr') is not None:
            self.cname_rr = m.get('CnameRr')

        if m.get('CnameType') is not None:
            self.cname_type = m.get('CnameType')

        if m.get('CnameZone') is not None:
            self.cname_zone = m.get('CnameZone')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

