# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class GetRecycleBinAttributeResponseBody(DaraModel):
    def __init__(
        self,
        recycle_bin_attribute: main_models.GetRecycleBinAttributeResponseBodyRecycleBinAttribute = None,
        request_id: str = None,
    ):
        # The description of the recycle bin.
        self.recycle_bin_attribute = recycle_bin_attribute
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.recycle_bin_attribute:
            self.recycle_bin_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recycle_bin_attribute is not None:
            result['RecycleBinAttribute'] = self.recycle_bin_attribute.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecycleBinAttribute') is not None:
            temp_model = main_models.GetRecycleBinAttributeResponseBodyRecycleBinAttribute()
            self.recycle_bin_attribute = temp_model.from_map(m.get('RecycleBinAttribute'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRecycleBinAttributeResponseBodyRecycleBinAttribute(DaraModel):
    def __init__(
        self,
        archive_size: int = None,
        enable_time: str = None,
        reserved_days: int = None,
        secondary_size: int = None,
        size: int = None,
        status: str = None,
    ):
        # The size of the archived data that is dumped to the recycle bin. Unit: bytes.
        self.archive_size = archive_size
        # The time at which the recycle bin was enabled.
        self.enable_time = enable_time
        # The retention period of the files in the recycle bin. Unit: days.
        # 
        # If the recycle bin is disabled, 0 is returned for this parameter.
        self.reserved_days = reserved_days
        # The size of the Infrequent Access (IA) data that is dumped to the recycle bin. Unit: bytes.
        self.secondary_size = secondary_size
        # The size of the files that are dumped to the recycle bin. Unit: bytes.
        self.size = size
        # The status of the recycle bin.
        # 
        # Valid values:
        # 
        # *   Enable: The recycle bin is enabled.
        # *   Disable: The recycle bin is disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_size is not None:
            result['ArchiveSize'] = self.archive_size

        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time

        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days

        if self.secondary_size is not None:
            result['SecondarySize'] = self.secondary_size

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveSize') is not None:
            self.archive_size = m.get('ArchiveSize')

        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')

        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')

        if m.get('SecondarySize') is not None:
            self.secondary_size = m.get('SecondarySize')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

