# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgenticTableEngineMeta(DaraModel):
    def __init__(
        self,
        checksum: str = None,
        create_time: str = None,
        data_bytes: int = None,
        encoding: str = None,
        engine: str = None,
        full_checksum: str = None,
        index_bytes: int = None,
        last_ddl_time: str = None,
        num_rows: int = None,
        ref_info: str = None,
        storage_capacity: int = None,
        table_schema_name: str = None,
    ):
        # The checksum of the table metadata.
        self.checksum = checksum
        # The time when the table was created. The format is yyyy-MM-dd HH:mm:ss.
        self.create_time = create_time
        # The data size of the table. Unit: bytes.
        self.data_bytes = data_bytes
        # The character set encoding of the table.
        self.encoding = encoding
        # The storage engine of the table.
        self.engine = engine
        # The full checksum of the table metadata.
        self.full_checksum = full_checksum
        # The index size of the table. Unit: bytes.
        self.index_bytes = index_bytes
        # The time when the last DDL operation was executed on the table. The format is yyyy-MM-dd HH:mm:ss.
        self.last_ddl_time = last_ddl_time
        # The number of rows in the table.
        self.num_rows = num_rows
        # The reference information of the table.
        self.ref_info = ref_info
        # The storage capacity of the table. Unit: MB.
        self.storage_capacity = storage_capacity
        # The name of the schema to which the table belongs.
        self.table_schema_name = table_schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checksum is not None:
            result['Checksum'] = self.checksum

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_bytes is not None:
            result['DataBytes'] = self.data_bytes

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.full_checksum is not None:
            result['FullChecksum'] = self.full_checksum

        if self.index_bytes is not None:
            result['IndexBytes'] = self.index_bytes

        if self.last_ddl_time is not None:
            result['LastDdlTime'] = self.last_ddl_time

        if self.num_rows is not None:
            result['NumRows'] = self.num_rows

        if self.ref_info is not None:
            result['RefInfo'] = self.ref_info

        if self.storage_capacity is not None:
            result['StorageCapacity'] = self.storage_capacity

        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataBytes') is not None:
            self.data_bytes = m.get('DataBytes')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('FullChecksum') is not None:
            self.full_checksum = m.get('FullChecksum')

        if m.get('IndexBytes') is not None:
            self.index_bytes = m.get('IndexBytes')

        if m.get('LastDdlTime') is not None:
            self.last_ddl_time = m.get('LastDdlTime')

        if m.get('NumRows') is not None:
            self.num_rows = m.get('NumRows')

        if m.get('RefInfo') is not None:
            self.ref_info = m.get('RefInfo')

        if m.get('StorageCapacity') is not None:
            self.storage_capacity = m.get('StorageCapacity')

        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')

        return self

