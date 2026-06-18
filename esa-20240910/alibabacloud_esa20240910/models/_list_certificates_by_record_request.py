# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCertificatesByRecordRequest(DaraModel):
    def __init__(
        self,
        detail: bool = None,
        record_name: str = None,
        site_id: int = None,
        valid_only: bool = None,
    ):
        # Specifies whether to return certificate details. A value of `1` includes certificate details, whereas a value of `0` excludes them.
        self.detail = detail
        # The record name.
        # 
        # This parameter is required.
        self.record_name = record_name
        # The site ID. To obtain this ID, call the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Specifies whether to return only valid certificates. A value of `1` returns only valid certificates, whereas `0` returns all matching certificates.
        self.valid_only = valid_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.valid_only is not None:
            result['ValidOnly'] = self.valid_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('ValidOnly') is not None:
            self.valid_only = m.get('ValidOnly')

        return self

