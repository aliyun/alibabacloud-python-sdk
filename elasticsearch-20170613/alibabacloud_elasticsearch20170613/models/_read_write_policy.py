# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadWritePolicy(DaraModel):
    def __init__(
        self,
        auto_generate_pk: bool = None,
        write_ha: bool = None,
        write_policy: str = None,
    ):
        # Specifies whether to automatically generate a document hash primary key when no primary key exists. Valid values:
        # 
        # - true (default): automatically generates a primary key.
        # - false: does not automatically generate a primary key.
        # 
        # >Notice:  autoGeneratePk cannot be modified independently. The autoGeneratePk setting takes effect only when writeHa is changed from false to true.
        # .
        self.auto_generate_pk = auto_generate_pk
        # Specifies whether to enable the write high-availability feature. Valid values:
        # 
        # - true: enabled.
        # - false: not enabled.
        self.write_ha = write_ha
        # Temporarily switches between synchronous and asynchronous high availability. Valid values:
        # 
        # - sync: temporarily switches from asynchronous write high availability to synchronous write.
        # - async: restores asynchronous write high availability after synchronous write is temporarily enabled.
        # 
        # > This field takes effect only when high availability is enabled, that is, writeHa is set to true. You do not need to pass in the writeHa field when setting this field.
        self.write_policy = write_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_generate_pk is not None:
            result['autoGeneratePk'] = self.auto_generate_pk

        if self.write_ha is not None:
            result['writeHa'] = self.write_ha

        if self.write_policy is not None:
            result['writePolicy'] = self.write_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoGeneratePk') is not None:
            self.auto_generate_pk = m.get('autoGeneratePk')

        if m.get('writeHa') is not None:
            self.write_ha = m.get('writeHa')

        if m.get('writePolicy') is not None:
            self.write_policy = m.get('writePolicy')

        return self

