# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSkillAuditRecordRequest(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        cid: str = None,
        dry_run_status: str = None,
        ext_info: str = None,
        record_type: str = None,
        script_transform_result: str = None,
        script_transform_status: str = None,
        source_dialect: str = None,
        source_sql_script: str = None,
        target_dialect: str = None,
    ):
        # The batch ID.
        self.batch_id = batch_id
        # The tenant ID.
        self.cid = cid
        # The dry run status.
        self.dry_run_status = dry_run_status
        # The extended information.
        self.ext_info = ext_info
        # The record type.
        self.record_type = record_type
        # The conversion result.
        self.script_transform_result = script_transform_result
        # The conversion status.
        self.script_transform_status = script_transform_status
        # The source dialect.
        self.source_dialect = source_dialect
        # The source dialect content.
        self.source_sql_script = source_sql_script
        # The target dialect.
        self.target_dialect = target_dialect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.cid is not None:
            result['cid'] = self.cid

        if self.dry_run_status is not None:
            result['dryRunStatus'] = self.dry_run_status

        if self.ext_info is not None:
            result['extInfo'] = self.ext_info

        if self.record_type is not None:
            result['recordType'] = self.record_type

        if self.script_transform_result is not None:
            result['scriptTransformResult'] = self.script_transform_result

        if self.script_transform_status is not None:
            result['scriptTransformStatus'] = self.script_transform_status

        if self.source_dialect is not None:
            result['sourceDialect'] = self.source_dialect

        if self.source_sql_script is not None:
            result['sourceSqlScript'] = self.source_sql_script

        if self.target_dialect is not None:
            result['targetDialect'] = self.target_dialect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('cid') is not None:
            self.cid = m.get('cid')

        if m.get('dryRunStatus') is not None:
            self.dry_run_status = m.get('dryRunStatus')

        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')

        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')

        if m.get('scriptTransformResult') is not None:
            self.script_transform_result = m.get('scriptTransformResult')

        if m.get('scriptTransformStatus') is not None:
            self.script_transform_status = m.get('scriptTransformStatus')

        if m.get('sourceDialect') is not None:
            self.source_dialect = m.get('sourceDialect')

        if m.get('sourceSqlScript') is not None:
            self.source_sql_script = m.get('sourceSqlScript')

        if m.get('targetDialect') is not None:
            self.target_dialect = m.get('targetDialect')

        return self

