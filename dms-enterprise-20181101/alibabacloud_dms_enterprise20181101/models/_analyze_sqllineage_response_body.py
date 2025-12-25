# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class AnalyzeSQLLineageResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        lineage_result: main_models.AnalyzeSQLLineageResponseBodyLineageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # Returned data set of SQL lineage.
        self.lineage_result = lineage_result
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.lineage_result:
            self.lineage_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.lineage_result is not None:
            result['LineageResult'] = self.lineage_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('LineageResult') is not None:
            temp_model = main_models.AnalyzeSQLLineageResponseBodyLineageResult()
            self.lineage_result = temp_model.from_map(m.get('LineageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AnalyzeSQLLineageResponseBodyLineageResult(DaraModel):
    def __init__(
        self,
        lineages: List[main_models.AnalyzeSQLLineageResponseBodyLineageResultLineages] = None,
        object_metadata: List[main_models.AnalyzeSQLLineageResponseBodyLineageResultObjectMetadata] = None,
    ):
        # The details about the lineage.
        self.lineages = lineages
        # The table and field metadata information.
        self.object_metadata = object_metadata

    def validate(self):
        if self.lineages:
            for v1 in self.lineages:
                 if v1:
                    v1.validate()
        if self.object_metadata:
            for v1 in self.object_metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Lineages'] = []
        if self.lineages is not None:
            for k1 in self.lineages:
                result['Lineages'].append(k1.to_map() if k1 else None)

        result['ObjectMetadata'] = []
        if self.object_metadata is not None:
            for k1 in self.object_metadata:
                result['ObjectMetadata'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lineages = []
        if m.get('Lineages') is not None:
            for k1 in m.get('Lineages'):
                temp_model = main_models.AnalyzeSQLLineageResponseBodyLineageResultLineages()
                self.lineages.append(temp_model.from_map(k1))

        self.object_metadata = []
        if m.get('ObjectMetadata') is not None:
            for k1 in m.get('ObjectMetadata'):
                temp_model = main_models.AnalyzeSQLLineageResponseBodyLineageResultObjectMetadata()
                self.object_metadata.append(temp_model.from_map(k1))

        return self

class AnalyzeSQLLineageResponseBodyLineageResultObjectMetadata(DaraModel):
    def __init__(
        self,
        fields: List[main_models.AnalyzeSQLLineageResponseBodyLineageResultObjectMetadataFields] = None,
        name: str = None,
        source: str = None,
        type: str = None,
    ):
        # The fields in the metatable.
        self.fields = fields
        # The object name.
        self.name = name
        # The source of metadata. Valid values:
        # 
        # *   **DDL**: The metadata comes from parsed SQL statements or definition of databases and tables collected by DMS.
        # *   **LINEAGE**: The metadata comes from lineage analysis results.
        self.source = source
        # The object type. Valid values:
        # 
        # *   **TABLE**
        # *   **VIEW**
        # *   **TMP_TABLE**
        self.type = type

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.source is not None:
            result['Source'] = self.source

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.AnalyzeSQLLineageResponseBodyLineageResultObjectMetadataFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AnalyzeSQLLineageResponseBodyLineageResultObjectMetadataFields(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the field.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class AnalyzeSQLLineageResponseBodyLineageResultLineages(DaraModel):
    def __init__(
        self,
        dst: str = None,
        lineage_type: str = None,
        oper_type: str = None,
        process_detail: main_models.AnalyzeSQLLineageResponseBodyLineageResultLineagesProcessDetail = None,
        src: str = None,
    ):
        # The target.
        self.dst = dst
        # The type of the lineage. Valid values:
        # 
        # *   **FIELD_DEPEND_FIELD**: Fields depend on fields.
        # *   **TABLE_DEPEND_TABLE**: Tables depend on tables.
        # *   **FIELD_INFLU_TABLE**: Fields influence tables.
        # *   **FIELD_INFLU_FIELD**: Fields influence fields.
        # *   **FIELD_INFLU_TABLE**: Tables influence fields.
        # *   **FIELD_JOIN_FIELD**: Fields are associated with fields.
        self.lineage_type = lineage_type
        # The operation type of the SQL statement in which the data lineage is generated. For example, if the operation type is SELECT, the data lineage is generated from a SELECT statement.
        # 
        # >  This field is an extended field which has no practical use.
        self.oper_type = oper_type
        # The handling details. This parameter is returned only when LineageType is FIELD_DEPEND_FIELD.
        self.process_detail = process_detail
        # The source.
        self.src = src

    def validate(self):
        if self.process_detail:
            self.process_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst is not None:
            result['Dst'] = self.dst

        if self.lineage_type is not None:
            result['LineageType'] = self.lineage_type

        if self.oper_type is not None:
            result['OperType'] = self.oper_type

        if self.process_detail is not None:
            result['ProcessDetail'] = self.process_detail.to_map()

        if self.src is not None:
            result['Src'] = self.src

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dst') is not None:
            self.dst = m.get('Dst')

        if m.get('LineageType') is not None:
            self.lineage_type = m.get('LineageType')

        if m.get('OperType') is not None:
            self.oper_type = m.get('OperType')

        if m.get('ProcessDetail') is not None:
            temp_model = main_models.AnalyzeSQLLineageResponseBodyLineageResultLineagesProcessDetail()
            self.process_detail = temp_model.from_map(m.get('ProcessDetail'))

        if m.get('Src') is not None:
            self.src = m.get('Src')

        return self

class AnalyzeSQLLineageResponseBodyLineageResultLineagesProcessDetail(DaraModel):
    def __init__(
        self,
        cal_way: str = None,
        code: str = None,
    ):
        # The calculating method. Valid values:
        # 
        # *   **DIRECT**: No function or expression is used.
        # *   **EXPR**: A function or expression is used.
        self.cal_way = cal_way
        # The SQL code snippet for field processing.
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cal_way is not None:
            result['CalWay'] = self.cal_way

        if self.code is not None:
            result['Code'] = self.code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalWay') is not None:
            self.cal_way = m.get('CalWay')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        return self

