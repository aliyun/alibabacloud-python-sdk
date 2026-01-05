# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachApplicationPolarFSRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        polar_fsaccess_key_id: str = None,
        polar_fsaccess_key_secret: str = None,
        polar_fsinstance_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.polar_fsaccess_key_id = polar_fsaccess_key_id
        self.polar_fsaccess_key_secret = polar_fsaccess_key_secret
        # This parameter is required.
        self.polar_fsinstance_id = polar_fsinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.polar_fsaccess_key_id is not None:
            result['PolarFSAccessKeyId'] = self.polar_fsaccess_key_id

        if self.polar_fsaccess_key_secret is not None:
            result['PolarFSAccessKeySecret'] = self.polar_fsaccess_key_secret

        if self.polar_fsinstance_id is not None:
            result['PolarFSInstanceId'] = self.polar_fsinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('PolarFSAccessKeyId') is not None:
            self.polar_fsaccess_key_id = m.get('PolarFSAccessKeyId')

        if m.get('PolarFSAccessKeySecret') is not None:
            self.polar_fsaccess_key_secret = m.get('PolarFSAccessKeySecret')

        if m.get('PolarFSInstanceId') is not None:
            self.polar_fsinstance_id = m.get('PolarFSInstanceId')

        return self

