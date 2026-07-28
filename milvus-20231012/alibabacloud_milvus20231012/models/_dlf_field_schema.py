# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DlfFieldSchema(DaraModel):
    def __init__(
        self,
        comment: str = None,
        dimension: int = None,
        dlf_field_type: str = None,
        field_name: str = None,
        is_primary_key: bool = None,
        is_supported: bool = None,
        is_vector_field: bool = None,
        milvus_field_type: str = None,
        nullable: bool = None,
        unsupported_reason: str = None,
    ):
        # A comment for the field.
        self.comment = comment
        # The dimension of the vector field. This parameter applies only when `isVectorField` is `true`.
        self.dimension = dimension
        # The DLF field type.
        self.dlf_field_type = dlf_field_type
        # The field name.
        self.field_name = field_name
        # Indicates whether the field is a primary key.
        self.is_primary_key = is_primary_key
        # Indicates whether the DLF field type can be mapped to a Milvus field type.
        self.is_supported = is_supported
        # Indicates whether the field is a vector field.
        self.is_vector_field = is_vector_field
        # The corresponding Milvus field type.
        self.milvus_field_type = milvus_field_type
        # Indicates whether the field can be null.
        self.nullable = nullable
        # The reason the DLF field type is unsupported. This field is present only when `isSupported` is `false`.
        self.unsupported_reason = unsupported_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.dimension is not None:
            result['dimension'] = self.dimension

        if self.dlf_field_type is not None:
            result['dlfFieldType'] = self.dlf_field_type

        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.is_primary_key is not None:
            result['isPrimaryKey'] = self.is_primary_key

        if self.is_supported is not None:
            result['isSupported'] = self.is_supported

        if self.is_vector_field is not None:
            result['isVectorField'] = self.is_vector_field

        if self.milvus_field_type is not None:
            result['milvusFieldType'] = self.milvus_field_type

        if self.nullable is not None:
            result['nullable'] = self.nullable

        if self.unsupported_reason is not None:
            result['unsupportedReason'] = self.unsupported_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')

        if m.get('dlfFieldType') is not None:
            self.dlf_field_type = m.get('dlfFieldType')

        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('isPrimaryKey') is not None:
            self.is_primary_key = m.get('isPrimaryKey')

        if m.get('isSupported') is not None:
            self.is_supported = m.get('isSupported')

        if m.get('isVectorField') is not None:
            self.is_vector_field = m.get('isVectorField')

        if m.get('milvusFieldType') is not None:
            self.milvus_field_type = m.get('milvusFieldType')

        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')

        if m.get('unsupportedReason') is not None:
            self.unsupported_reason = m.get('unsupportedReason')

        return self

