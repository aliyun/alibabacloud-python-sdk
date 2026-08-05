# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExperienceDataRequest(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        dry_run: bool = None,
        service_type: str = None,
    ):
        # The data type.
        self.data_type = data_type
        # - true
        # - false.
        self.dry_run = dry_run
        # The service type.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        return self

