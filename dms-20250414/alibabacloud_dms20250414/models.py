# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class DLCatalog(TeaModel):
    def __init__(
        self,
        description: str = None,
        location: str = None,
        name: str = None,
    ):
        self.description = description
        self.location = location
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DLColumn(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DLDatabase(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_id: int = None,
        description: str = None,
        location: str = None,
        name: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.catalog_name = catalog_name
        self.db_id = db_id
        self.description = description
        self.location = location
        self.name = name
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class DLResourceUri(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        uri: str = None,
    ):
        self.resource_type = resource_type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DLFunction(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        class_name: str = None,
        create_time: int = None,
        creator_id: int = None,
        db_name: str = None,
        function_name: str = None,
        function_type: str = None,
        modifier_id: int = None,
        owner_name: str = None,
        owner_type: str = None,
        resource_uris: List[DLResourceUri] = None,
    ):
        self.catalog_name = catalog_name
        self.class_name = class_name
        self.create_time = create_time
        self.creator_id = creator_id
        self.db_name = db_name
        self.function_name = function_name
        self.function_type = function_type
        self.modifier_id = modifier_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.resource_uris = resource_uris

    def validate(self):
        if self.resource_uris:
            for k in self.resource_uris:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        result['ResourceUris'] = []
        if self.resource_uris is not None:
            for k in self.resource_uris:
                result['ResourceUris'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        self.resource_uris = []
        if m.get('ResourceUris') is not None:
            for k in m.get('ResourceUris'):
                temp_model = DLResourceUri()
                self.resource_uris.append(temp_model.from_map(k))
        return self


class DLFunctionInput(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        create_time: int = None,
        creator_id: int = None,
        function_name: str = None,
        function_type: str = None,
        modifier_id: int = None,
        owner_name: str = None,
        owner_type: str = None,
        resource_uris: List[DLResourceUri] = None,
    ):
        self.class_name = class_name
        self.create_time = create_time
        self.creator_id = creator_id
        self.function_name = function_name
        self.function_type = function_type
        self.modifier_id = modifier_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.resource_uris = resource_uris

    def validate(self):
        if self.resource_uris:
            for k in self.resource_uris:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        result['ResourceUris'] = []
        if self.resource_uris is not None:
            for k in self.resource_uris:
                result['ResourceUris'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        self.resource_uris = []
        if m.get('ResourceUris') is not None:
            for k in m.get('ResourceUris'):
                temp_model = DLResourceUri()
                self.resource_uris.append(temp_model.from_map(k))
        return self


class DLOrder(TeaModel):
    def __init__(
        self,
        col: str = None,
        order: int = None,
    ):
        self.col = col
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.col is not None:
            result['Col'] = self.col
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Col') is not None:
            self.col = m.get('Col')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class DLSerdeInfo(TeaModel):
    def __init__(
        self,
        description: str = None,
        deserializer_class: str = None,
        name: str = None,
        parameters: Dict[str, Any] = None,
        serde_type: int = None,
        serialization_lib: str = None,
        serializer_class: str = None,
    ):
        self.description = description
        self.deserializer_class = deserializer_class
        self.name = name
        self.parameters = parameters
        self.serde_type = serde_type
        self.serialization_lib = serialization_lib
        self.serializer_class = serializer_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.deserializer_class is not None:
            result['DeserializerClass'] = self.deserializer_class
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serde_type is not None:
            result['SerdeType'] = self.serde_type
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        if self.serializer_class is not None:
            result['SerializerClass'] = self.serializer_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeserializerClass') is not None:
            self.deserializer_class = m.get('DeserializerClass')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerdeType') is not None:
            self.serde_type = m.get('SerdeType')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        if m.get('SerializerClass') is not None:
            self.serializer_class = m.get('SerializerClass')
        return self


class DLSkewedInfo(TeaModel):
    def __init__(
        self,
        skewed_col_names: List[str] = None,
        skewed_col_value_location_maps: Dict[str, Any] = None,
        skewed_col_values: List[List[str]] = None,
    ):
        self.skewed_col_names = skewed_col_names
        self.skewed_col_value_location_maps = skewed_col_value_location_maps
        self.skewed_col_values = skewed_col_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skewed_col_names is not None:
            result['SkewedColNames'] = self.skewed_col_names
        if self.skewed_col_value_location_maps is not None:
            result['SkewedColValueLocationMaps'] = self.skewed_col_value_location_maps
        if self.skewed_col_values is not None:
            result['SkewedColValues'] = self.skewed_col_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkewedColNames') is not None:
            self.skewed_col_names = m.get('SkewedColNames')
        if m.get('SkewedColValueLocationMaps') is not None:
            self.skewed_col_value_location_maps = m.get('SkewedColValueLocationMaps')
        if m.get('SkewedColValues') is not None:
            self.skewed_col_values = m.get('SkewedColValues')
        return self


class DLStorageDescriptor(TeaModel):
    def __init__(
        self,
        bucket_cols: List[str] = None,
        columns: List[DLColumn] = None,
        input_format: str = None,
        is_compressed: bool = None,
        location: str = None,
        num_buckets: int = None,
        original_columns: List[DLColumn] = None,
        output_format: str = None,
        parameters: Dict[str, Any] = None,
        serde_info: DLSerdeInfo = None,
        skewed_info: DLSkewedInfo = None,
        sort_cols: List[DLOrder] = None,
    ):
        self.bucket_cols = bucket_cols
        self.columns = columns
        self.input_format = input_format
        self.is_compressed = is_compressed
        self.location = location
        self.num_buckets = num_buckets
        self.original_columns = original_columns
        self.output_format = output_format
        self.parameters = parameters
        self.serde_info = serde_info
        self.skewed_info = skewed_info
        self.sort_cols = sort_cols

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()
        if self.original_columns:
            for k in self.original_columns:
                if k:
                    k.validate()
        if self.serde_info:
            self.serde_info.validate()
        if self.skewed_info:
            self.skewed_info.validate()
        if self.sort_cols:
            for k in self.sort_cols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_cols is not None:
            result['BucketCols'] = self.bucket_cols
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.is_compressed is not None:
            result['IsCompressed'] = self.is_compressed
        if self.location is not None:
            result['Location'] = self.location
        if self.num_buckets is not None:
            result['NumBuckets'] = self.num_buckets
        result['OriginalColumns'] = []
        if self.original_columns is not None:
            for k in self.original_columns:
                result['OriginalColumns'].append(k.to_map() if k else None)
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serde_info is not None:
            result['SerdeInfo'] = self.serde_info.to_map()
        if self.skewed_info is not None:
            result['SkewedInfo'] = self.skewed_info.to_map()
        result['SortCols'] = []
        if self.sort_cols is not None:
            for k in self.sort_cols:
                result['SortCols'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCols') is not None:
            self.bucket_cols = m.get('BucketCols')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = DLColumn()
                self.columns.append(temp_model.from_map(k))
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('IsCompressed') is not None:
            self.is_compressed = m.get('IsCompressed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('NumBuckets') is not None:
            self.num_buckets = m.get('NumBuckets')
        self.original_columns = []
        if m.get('OriginalColumns') is not None:
            for k in m.get('OriginalColumns'):
                temp_model = DLColumn()
                self.original_columns.append(temp_model.from_map(k))
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerdeInfo') is not None:
            temp_model = DLSerdeInfo()
            self.serde_info = temp_model.from_map(m['SerdeInfo'])
        if m.get('SkewedInfo') is not None:
            temp_model = DLSkewedInfo()
            self.skewed_info = temp_model.from_map(m['SkewedInfo'])
        self.sort_cols = []
        if m.get('SortCols') is not None:
            for k in m.get('SortCols'):
                temp_model = DLOrder()
                self.sort_cols.append(temp_model.from_map(k))
        return self


class DLPartition(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        create_time: int = None,
        db_name: str = None,
        last_access_time: int = None,
        parameters: Dict[str, str] = None,
        sd: DLStorageDescriptor = None,
        table_name: str = None,
        values: List[str] = None,
    ):
        self.catalog_name = catalog_name
        self.create_time = create_time
        self.db_name = db_name
        self.last_access_time = last_access_time
        self.parameters = parameters
        self.sd = sd
        self.table_name = table_name
        self.values = values

    def validate(self):
        if self.sd:
            self.sd.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.sd is not None:
            result['Sd'] = self.sd.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Sd') is not None:
            temp_model = DLStorageDescriptor()
            self.sd = temp_model.from_map(m['Sd'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DLPartitionInput(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        last_access_time: int = None,
        parameters: Dict[str, str] = None,
        storage_descriptor: DLStorageDescriptor = None,
        values: List[str] = None,
    ):
        self.create_time = create_time
        self.last_access_time = last_access_time
        self.parameters = parameters
        self.storage_descriptor = storage_descriptor
        self.values = values

    def validate(self):
        if self.storage_descriptor:
            self.storage_descriptor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.storage_descriptor is not None:
            result['StorageDescriptor'] = self.storage_descriptor.to_map()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('StorageDescriptor') is not None:
            temp_model = DLStorageDescriptor()
            self.storage_descriptor = temp_model.from_map(m['StorageDescriptor'])
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DLTable(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        create_time: int = None,
        creator_id: int = None,
        db_id: int = None,
        db_name: str = None,
        description: str = None,
        last_access_time: int = None,
        location: str = None,
        modifier_id: int = None,
        name: str = None,
        owner: str = None,
        owner_type: str = None,
        parameters: Dict[str, Any] = None,
        partition_keys: List[DLColumn] = None,
        retention: int = None,
        storage_descriptor: DLStorageDescriptor = None,
        table_type: str = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
    ):
        self.catalog_name = catalog_name
        self.create_time = create_time
        self.creator_id = creator_id
        self.db_id = db_id
        self.db_name = db_name
        self.description = description
        self.last_access_time = last_access_time
        self.location = location
        self.modifier_id = modifier_id
        self.name = name
        self.owner = owner
        self.owner_type = owner_type
        self.parameters = parameters
        self.partition_keys = partition_keys
        self.retention = retention
        self.storage_descriptor = storage_descriptor
        self.table_type = table_type
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text

    def validate(self):
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()
        if self.storage_descriptor:
            self.storage_descriptor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.description is not None:
            result['Description'] = self.description
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.location is not None:
            result['Location'] = self.location
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.storage_descriptor is not None:
            result['StorageDescriptor'] = self.storage_descriptor.to_map()
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = DLColumn()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('StorageDescriptor') is not None:
            temp_model = DLStorageDescriptor()
            self.storage_descriptor = temp_model.from_map(m['StorageDescriptor'])
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        return self


class DLTableInput(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        creator_id: int = None,
        description: str = None,
        last_access_time: int = None,
        location: str = None,
        modifier_id: int = None,
        name: str = None,
        owner: str = None,
        owner_type: str = None,
        parameters: Dict[str, str] = None,
        partition_keys: List[DLColumn] = None,
        retention: int = None,
        storage_descriptor: DLStorageDescriptor = None,
        table_type: str = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
    ):
        self.create_time = create_time
        self.creator_id = creator_id
        self.description = description
        self.last_access_time = last_access_time
        self.location = location
        self.modifier_id = modifier_id
        self.name = name
        self.owner = owner
        self.owner_type = owner_type
        self.parameters = parameters
        self.partition_keys = partition_keys
        self.retention = retention
        self.storage_descriptor = storage_descriptor
        self.table_type = table_type
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text

    def validate(self):
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()
        if self.storage_descriptor:
            self.storage_descriptor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.location is not None:
            result['Location'] = self.location
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.storage_descriptor is not None:
            result['StorageDescriptor'] = self.storage_descriptor.to_map()
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = DLColumn()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('StorageDescriptor') is not None:
            temp_model = DLStorageDescriptor()
            self.storage_descriptor = temp_model.from_map(m['StorageDescriptor'])
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        return self


class DLTablebaseInfo(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        create_time: int = None,
        creator_id: int = None,
        db_id: int = None,
        db_name: str = None,
        description: str = None,
        last_access_time: int = None,
        location: str = None,
        modifier_id: int = None,
        name: str = None,
        owner: str = None,
        owner_type: str = None,
        parameters: Dict[str, Any] = None,
        partition_keys: List[DLColumn] = None,
        retention: int = None,
        table_type: str = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
    ):
        self.catalog_name = catalog_name
        self.create_time = create_time
        self.creator_id = creator_id
        self.db_id = db_id
        self.db_name = db_name
        self.description = description
        self.last_access_time = last_access_time
        self.location = location
        self.modifier_id = modifier_id
        self.name = name
        self.owner = owner
        self.owner_type = owner_type
        self.parameters = parameters
        self.partition_keys = partition_keys
        self.retention = retention
        self.table_type = table_type
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text

    def validate(self):
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.description is not None:
            result['Description'] = self.description
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.location is not None:
            result['Location'] = self.location
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = DLColumn()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        return self


class ForeignInstance(TeaModel):
    def __init__(
        self,
        data_link_name: str = None,
        host: str = None,
        instance_source: str = None,
        instance_type: str = None,
        port: int = None,
        properties: Dict[str, str] = None,
        region_id: str = None,
        sid: str = None,
    ):
        self.data_link_name = data_link_name
        self.host = host
        self.instance_source = instance_source
        self.instance_type = instance_type
        self.port = port
        self.properties = properties
        self.region_id = region_id
        self.sid = sid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sid is not None:
            result['Sid'] = self.sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        return self


class ForeignInstanceCredInfo(TeaModel):
    def __init__(
        self,
        cred_info: Dict[str, str] = None,
        cred_type: str = None,
    ):
        self.cred_info = cred_info
        self.cred_type = cred_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cred_info is not None:
            result['CredInfo'] = self.cred_info
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredInfo') is not None:
            self.cred_info = m.get('CredInfo')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        return self


class PartitionError(TeaModel):
    def __init__(
        self,
        error_detail: str = None,
        values: List[str] = None,
    ):
        self.error_detail = error_detail
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class BatchCreateDataLakePartitionsRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        if_not_exists: bool = None,
        need_result: bool = None,
        partition_inputs: List[DLPartitionInput] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.if_not_exists = if_not_exists
        self.need_result = need_result
        # This parameter is required.
        self.partition_inputs = partition_inputs
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.partition_inputs:
            for k in self.partition_inputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.if_not_exists is not None:
            result['IfNotExists'] = self.if_not_exists
        if self.need_result is not None:
            result['NeedResult'] = self.need_result
        result['PartitionInputs'] = []
        if self.partition_inputs is not None:
            for k in self.partition_inputs:
                result['PartitionInputs'].append(k.to_map() if k else None)
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('IfNotExists') is not None:
            self.if_not_exists = m.get('IfNotExists')
        if m.get('NeedResult') is not None:
            self.need_result = m.get('NeedResult')
        self.partition_inputs = []
        if m.get('PartitionInputs') is not None:
            for k in m.get('PartitionInputs'):
                temp_model = DLPartitionInput()
                self.partition_inputs.append(temp_model.from_map(k))
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class BatchCreateDataLakePartitionsShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        if_not_exists: bool = None,
        need_result: bool = None,
        partition_inputs_shrink: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.if_not_exists = if_not_exists
        self.need_result = need_result
        # This parameter is required.
        self.partition_inputs_shrink = partition_inputs_shrink
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.if_not_exists is not None:
            result['IfNotExists'] = self.if_not_exists
        if self.need_result is not None:
            result['NeedResult'] = self.need_result
        if self.partition_inputs_shrink is not None:
            result['PartitionInputs'] = self.partition_inputs_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('IfNotExists') is not None:
            self.if_not_exists = m.get('IfNotExists')
        if m.get('NeedResult') is not None:
            self.need_result = m.get('NeedResult')
        if m.get('PartitionInputs') is not None:
            self.partition_inputs_shrink = m.get('PartitionInputs')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class BatchCreateDataLakePartitionsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        partitions: List[DLPartition] = None,
        request_id: str = None,
        success: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.partitions = partitions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['Partitions'].append(k.to_map() if k else None)
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
        self.partitions = []
        if m.get('Partitions') is not None:
            for k in m.get('Partitions'):
                temp_model = DLPartition()
                self.partitions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchCreateDataLakePartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateDataLakePartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchCreateDataLakePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteDataLakePartitionsRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        if_exists: bool = None,
        partition_values_list: List[List[str]] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.if_exists = if_exists
        # This parameter is required.
        self.partition_values_list = partition_values_list
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.if_exists is not None:
            result['IfExists'] = self.if_exists
        if self.partition_values_list is not None:
            result['PartitionValuesList'] = self.partition_values_list
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('IfExists') is not None:
            self.if_exists = m.get('IfExists')
        if m.get('PartitionValuesList') is not None:
            self.partition_values_list = m.get('PartitionValuesList')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class BatchDeleteDataLakePartitionsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        partition_errors: List[PartitionError] = None,
        request_id: str = None,
        success: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.partition_errors = partition_errors
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_errors:
            for k in self.partition_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['PartitionErrors'] = []
        if self.partition_errors is not None:
            for k in self.partition_errors:
                result['PartitionErrors'].append(k.to_map() if k else None)
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
        self.partition_errors = []
        if m.get('PartitionErrors') is not None:
            for k in m.get('PartitionErrors'):
                temp_model = PartitionError()
                self.partition_errors.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchDeleteDataLakePartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteDataLakePartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteDataLakePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateDataLakePartitionsRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        partition_inputs: List[DLPartitionInput] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.partition_inputs = partition_inputs
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.partition_inputs:
            for k in self.partition_inputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        result['PartitionInputs'] = []
        if self.partition_inputs is not None:
            for k in self.partition_inputs:
                result['PartitionInputs'].append(k.to_map() if k else None)
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        self.partition_inputs = []
        if m.get('PartitionInputs') is not None:
            for k in m.get('PartitionInputs'):
                temp_model = DLPartitionInput()
                self.partition_inputs.append(temp_model.from_map(k))
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class BatchUpdateDataLakePartitionsShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        partition_inputs_shrink: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.partition_inputs_shrink = partition_inputs_shrink
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.partition_inputs_shrink is not None:
            result['PartitionInputs'] = self.partition_inputs_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('PartitionInputs') is not None:
            self.partition_inputs_shrink = m.get('PartitionInputs')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class BatchUpdateDataLakePartitionsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        partition_errors: List[PartitionError] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.partition_errors = partition_errors
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_errors:
            for k in self.partition_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['PartitionErrors'] = []
        if self.partition_errors is not None:
            for k in self.partition_errors:
                result['PartitionErrors'].append(k.to_map() if k else None)
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
        self.partition_errors = []
        if m.get('PartitionErrors') is not None:
            for k in m.get('PartitionErrors'):
                temp_model = PartitionError()
                self.partition_errors.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchUpdateDataLakePartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateDataLakePartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchUpdateDataLakePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAirflowRequest(TeaModel):
    def __init__(
        self,
        airflow_name: str = None,
        app_spec: str = None,
        client_token: str = None,
        dags_dir: str = None,
        description: str = None,
        oss_bucket_name: str = None,
        oss_path: str = None,
        plugins_dir: str = None,
        requirement_file: str = None,
        security_group_id: str = None,
        startup_file: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.airflow_name = airflow_name
        # This parameter is required.
        self.app_spec = app_spec
        self.client_token = client_token
        self.dags_dir = dags_dir
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # This parameter is required.
        self.oss_path = oss_path
        self.plugins_dir = plugins_dir
        self.requirement_file = requirement_file
        # This parameter is required.
        self.security_group_id = security_group_id
        self.startup_file = startup_file
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.worker_serverless_replicas = worker_serverless_replicas
        # This parameter is required.
        self.workspace_id = workspace_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name
        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir
        if self.description is not None:
            result['Description'] = self.description
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir
        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.worker_serverless_replicas is not None:
            result['WorkerServerlessReplicas'] = self.worker_serverless_replicas
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')
        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')
        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkerServerlessReplicas') is not None:
            self.worker_serverless_replicas = m.get('WorkerServerlessReplicas')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateAirflowResponseBodyRoot(TeaModel):
    def __init__(
        self,
        airflow_id: str = None,
        airflow_name: str = None,
        app_spec: str = None,
        app_type: str = None,
        dags_dir: str = None,
        deploy_error_msg: str = None,
        description: str = None,
        gmt_created: str = None,
        oss_bucket_name: str = None,
        oss_path: str = None,
        plugins_dir: str = None,
        requirement_file: str = None,
        security_group_id: str = None,
        startup_file: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        self.airflow_id = airflow_id
        self.airflow_name = airflow_name
        self.app_spec = app_spec
        self.app_type = app_type
        self.dags_dir = dags_dir
        self.deploy_error_msg = deploy_error_msg
        self.description = description
        self.gmt_created = gmt_created
        self.oss_bucket_name = oss_bucket_name
        self.oss_path = oss_path
        self.plugins_dir = plugins_dir
        self.requirement_file = requirement_file
        self.security_group_id = security_group_id
        self.startup_file = startup_file
        self.status = status
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id
        self.worker_serverless_replicas = worker_serverless_replicas
        self.workspace_id = workspace_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id
        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name
        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir
        if self.deploy_error_msg is not None:
            result['DeployErrorMsg'] = self.deploy_error_msg
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir
        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.worker_serverless_replicas is not None:
            result['WorkerServerlessReplicas'] = self.worker_serverless_replicas
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')
        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')
        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')
        if m.get('DeployErrorMsg') is not None:
            self.deploy_error_msg = m.get('DeployErrorMsg')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')
        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkerServerlessReplicas') is not None:
            self.worker_serverless_replicas = m.get('WorkerServerlessReplicas')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateAirflowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        root: CreateAirflowResponseBodyRoot = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            temp_model = CreateAirflowResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAirflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAirflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAirflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAirflowLoginTokenRequest(TeaModel):
    def __init__(
        self,
        airflow_id: str = None,
    ):
        # The ID of the Airflow instance. You can view the instance ID on the [Airflow Instances](https://help.aliyun.com/document_detail/2881043.html) page.
        # 
        # This parameter is required.
        self.airflow_id = airflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')
        return self


class CreateAirflowLoginTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        host: str = None,
        token: str = None,
    ):
        # The endpoint that is used to access the Airflow instance.
        self.host = host
        # The generated token.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateAirflowLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateAirflowLoginTokenResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The result of the site monitoring task.
        self.data = data
        # The error code returned if the call failed. Variable description:
        # 
        # *   If the request was successful, this parameter is not returned.
        # *   This parameter is returned only if the request failed.
        # 
        # For more information, see the "Error codes" section in this topic.
        self.error_code = error_code
        # The description of the error code.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The request ID. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   True
        # *   False
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateAirflowLoginTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAirflowLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAirflowLoginTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAirflowLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataLakeDatabaseRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        description: str = None,
        location: str = None,
        parameters: Dict[str, str] = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.description = description
        # This parameter is required.
        self.location = location
        self.parameters = parameters
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDataLakeDatabaseShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        description: str = None,
        location: str = None,
        parameters_shrink: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.description = description
        # This parameter is required.
        self.location = location
        self.parameters_shrink = parameters_shrink
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDataLakeDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataLakeDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataLakeDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataLakeDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataLakeFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_input: DLFunctionInput = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.function_input = function_input
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.function_input:
            self.function_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_input is not None:
            result['FunctionInput'] = self.function_input.to_map()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionInput') is not None:
            temp_model = DLFunctionInput()
            self.function_input = temp_model.from_map(m['FunctionInput'])
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDataLakeFunctionShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_input_shrink: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.function_input_shrink = function_input_shrink
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_input_shrink is not None:
            result['FunctionInput'] = self.function_input_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionInput') is not None:
            self.function_input_shrink = m.get('FunctionInput')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDataLakeFunctionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        function: DLFunction = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.function = function
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.function is not None:
            result['Function'] = self.function.to_map()
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
        if m.get('Function') is not None:
            temp_model = DLFunction()
            self.function = temp_model.from_map(m['Function'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataLakeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataLakeFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataLakeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataLakePartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        if_not_exists: bool = None,
        need_result: bool = None,
        partition_input: DLPartitionInput = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.if_not_exists = if_not_exists
        self.need_result = need_result
        # This parameter is required.
        self.partition_input = partition_input
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.partition_input:
            self.partition_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.if_not_exists is not None:
            result['IfNotExists'] = self.if_not_exists
        if self.need_result is not None:
            result['NeedResult'] = self.need_result
        if self.partition_input is not None:
            result['PartitionInput'] = self.partition_input.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('IfNotExists') is not None:
            self.if_not_exists = m.get('IfNotExists')
        if m.get('NeedResult') is not None:
            self.need_result = m.get('NeedResult')
        if m.get('PartitionInput') is not None:
            temp_model = DLPartitionInput()
            self.partition_input = temp_model.from_map(m['PartitionInput'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDataLakePartitionShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        if_not_exists: bool = None,
        need_result: bool = None,
        partition_input_shrink: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.if_not_exists = if_not_exists
        self.need_result = need_result
        # This parameter is required.
        self.partition_input_shrink = partition_input_shrink
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.if_not_exists is not None:
            result['IfNotExists'] = self.if_not_exists
        if self.need_result is not None:
            result['NeedResult'] = self.need_result
        if self.partition_input_shrink is not None:
            result['PartitionInput'] = self.partition_input_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('IfNotExists') is not None:
            self.if_not_exists = m.get('IfNotExists')
        if m.get('NeedResult') is not None:
            self.need_result = m.get('NeedResult')
        if m.get('PartitionInput') is not None:
            self.partition_input_shrink = m.get('PartitionInput')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDataLakePartitionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        partition: DLPartition = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.partition = partition
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition:
            self.partition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.partition is not None:
            result['Partition'] = self.partition.to_map()
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
        if m.get('Partition') is not None:
            temp_model = DLPartition()
            self.partition = temp_model.from_map(m['Partition'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataLakePartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataLakePartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataLakePartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataLakeTableRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        table_input: DLTableInput = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.table_input = table_input
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.table_input:
            self.table_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_input is not None:
            result['TableInput'] = self.table_input.to_map()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableInput') is not None:
            temp_model = DLTableInput()
            self.table_input = temp_model.from_map(m['TableInput'])
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDataLakeTableShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        table_input_shrink: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.table_input_shrink = table_input_shrink
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_input_shrink is not None:
            result['TableInput'] = self.table_input_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableInput') is not None:
            self.table_input_shrink = m.get('TableInput')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDataLakeTableResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        table: DLTable = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.table = table

    def validate(self):
        if self.table:
            self.table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table is not None:
            result['Table'] = self.table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Table') is not None:
            temp_model = DLTable()
            self.table = temp_model.from_map(m['Table'])
        return self


class CreateDataLakeTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataLakeTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataLakeTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAirflowRequest(TeaModel):
    def __init__(
        self,
        airflow_id: str = None,
        client_token: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.airflow_id = airflow_id
        self.client_token = client_token
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteAirflowResponseBodyRootResponses(TeaModel):
    def __init__(
        self,
        success: bool = None,
        uuid: str = None,
    ):
        self.success = success
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DeleteAirflowResponseBodyRoot(TeaModel):
    def __init__(
        self,
        responses: List[DeleteAirflowResponseBodyRootResponses] = None,
    ):
        self.responses = responses

    def validate(self):
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['Responses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.responses = []
        if m.get('Responses') is not None:
            for k in m.get('Responses'):
                temp_model = DeleteAirflowResponseBodyRootResponses()
                self.responses.append(temp_model.from_map(k))
        return self


class DeleteAirflowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        root: DeleteAirflowResponseBodyRoot = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            temp_model = DeleteAirflowResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAirflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAirflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAirflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLakeDatabaseRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteDataLakeDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataLakeDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataLakeDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataLakeDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLakeFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.function_name = function_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteDataLakeFunctionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataLakeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataLakeFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataLakeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLakePartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        if_exists: bool = None,
        partition_values: List[str] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.if_exists = if_exists
        # This parameter is required.
        self.partition_values = partition_values
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.if_exists is not None:
            result['IfExists'] = self.if_exists
        if self.partition_values is not None:
            result['PartitionValues'] = self.partition_values
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('IfExists') is not None:
            self.if_exists = m.get('IfExists')
        if m.get('PartitionValues') is not None:
            self.partition_values = m.get('PartitionValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteDataLakePartitionShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        if_exists: bool = None,
        partition_values_shrink: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.if_exists = if_exists
        # This parameter is required.
        self.partition_values_shrink = partition_values_shrink
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.if_exists is not None:
            result['IfExists'] = self.if_exists
        if self.partition_values_shrink is not None:
            result['PartitionValues'] = self.partition_values_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('IfExists') is not None:
            self.if_exists = m.get('IfExists')
        if m.get('PartitionValues') is not None:
            self.partition_values_shrink = m.get('PartitionValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteDataLakePartitionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataLakePartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataLakePartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataLakePartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLakeTableRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteDataLakeTableResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataLakeTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataLakeTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataLakeTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAirflowRequest(TeaModel):
    def __init__(
        self,
        airflow_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.airflow_id = airflow_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetAirflowResponseBodyRoot(TeaModel):
    def __init__(
        self,
        airflow_id: str = None,
        airflow_name: str = None,
        app_spec: str = None,
        app_type: str = None,
        custom_airflow_cfg: List[str] = None,
        dags_dir: str = None,
        deploy_error_msg: str = None,
        description: str = None,
        gmt_created: str = None,
        oss_bucket_name: str = None,
        oss_path: str = None,
        plugins_dir: str = None,
        region_id: str = None,
        requirement_file: str = None,
        security_group_id: str = None,
        startup_file: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        self.airflow_id = airflow_id
        self.airflow_name = airflow_name
        self.app_spec = app_spec
        self.app_type = app_type
        self.custom_airflow_cfg = custom_airflow_cfg
        self.dags_dir = dags_dir
        self.deploy_error_msg = deploy_error_msg
        self.description = description
        self.gmt_created = gmt_created
        self.oss_bucket_name = oss_bucket_name
        self.oss_path = oss_path
        self.plugins_dir = plugins_dir
        self.region_id = region_id
        self.requirement_file = requirement_file
        self.security_group_id = security_group_id
        self.startup_file = startup_file
        self.status = status
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id
        self.worker_serverless_replicas = worker_serverless_replicas
        self.workspace_id = workspace_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id
        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name
        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.custom_airflow_cfg is not None:
            result['CustomAirflowCfg'] = self.custom_airflow_cfg
        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir
        if self.deploy_error_msg is not None:
            result['DeployErrorMsg'] = self.deploy_error_msg
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.worker_serverless_replicas is not None:
            result['WorkerServerlessReplicas'] = self.worker_serverless_replicas
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')
        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')
        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CustomAirflowCfg') is not None:
            self.custom_airflow_cfg = m.get('CustomAirflowCfg')
        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')
        if m.get('DeployErrorMsg') is not None:
            self.deploy_error_msg = m.get('DeployErrorMsg')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkerServerlessReplicas') is not None:
            self.worker_serverless_replicas = m.get('WorkerServerlessReplicas')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetAirflowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        root: GetAirflowResponseBodyRoot = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        # Reuqest ID。
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            temp_model = GetAirflowResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAirflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAirflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAirflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatContentRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        checkpoint: str = None,
        dmsunit: str = None,
        session_id: str = None,
    ):
        self.agent_id = agent_id
        self.checkpoint = checkpoint
        self.dmsunit = dmsunit
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GetChatContentResponseBody(TeaModel):
    def __init__(
        self,
        category: str = None,
        checkpoint: int = None,
        content: str = None,
        content_type: str = None,
        event_type: str = None,
        level: int = None,
    ):
        self.category = category
        self.checkpoint = checkpoint
        self.content = content
        self.content_type = content_type
        self.event_type = event_type
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.event_type is not None:
            result['event_type'] = self.event_type
        if self.level is not None:
            result['level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('event_type') is not None:
            self.event_type = m.get('event_type')
        if m.get('level') is not None:
            self.level = m.get('level')
        return self


class GetChatContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataLakeCatalogRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDataLakeCatalogResponseBody(TeaModel):
    def __init__(
        self,
        catalog: DLCatalog = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.catalog = catalog
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.catalog:
            self.catalog.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog is not None:
            result['Catalog'] = self.catalog.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            temp_model = DLCatalog()
            self.catalog = temp_model.from_map(m['Catalog'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataLakeCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataLakeCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataLakeCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataLakeDatabaseRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.name = name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.name is not None:
            result['Name'] = self.name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDataLakeDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        database: DLDatabase = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.database = database
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = DLDatabase()
            self.database = temp_model.from_map(m['Database'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataLakeDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataLakeDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataLakeDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataLakeFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.function_name = function_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDataLakeFunctionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        function: DLFunction = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.function = function
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.function is not None:
            result['Function'] = self.function.to_map()
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
        if m.get('Function') is not None:
            temp_model = DLFunction()
            self.function = temp_model.from_map(m['Function'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataLakeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataLakeFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataLakeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataLakePartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        partition_values: List[str] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.partition_values = partition_values
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.partition_values is not None:
            result['PartitionValues'] = self.partition_values
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('PartitionValues') is not None:
            self.partition_values = m.get('PartitionValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDataLakePartitionShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        partition_values_shrink: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.partition_values_shrink = partition_values_shrink
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.partition_values_shrink is not None:
            result['PartitionValues'] = self.partition_values_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('PartitionValues') is not None:
            self.partition_values_shrink = m.get('PartitionValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDataLakePartitionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        partition: DLPartition = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.partition = partition
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition:
            self.partition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.partition is not None:
            result['Partition'] = self.partition.to_map()
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
        if m.get('Partition') is not None:
            temp_model = DLPartition()
            self.partition = temp_model.from_map(m['Partition'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataLakePartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataLakePartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataLakePartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataLakeTableRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.name = name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.name is not None:
            result['Name'] = self.name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDataLakeTableResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: str = None,
        table: DLTable = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.table = table

    def validate(self):
        if self.table:
            self.table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table is not None:
            result['Table'] = self.table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Table') is not None:
            temp_model = DLTable()
            self.table = temp_model.from_map(m['Table'])
        return self


class GetDataLakeTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataLakeTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataLakeTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNotebookAndSubmitTaskRequest(TeaModel):
    def __init__(
        self,
        params: str = None,
        path: str = None,
        retry: int = None,
        session_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.params = params
        # This parameter is required.
        self.path = path
        self.retry = retry
        # This parameter is required.
        self.session_id = session_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.path is not None:
            result['Path'] = self.path
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetNotebookAndSubmitTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        err_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        session_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.err_msg = err_msg
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.session_id = session_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetNotebookAndSubmitTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNotebookAndSubmitTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNotebookAndSubmitTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNotebookTaskStatusRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        self.session_id = session_id
        self.task_id = task_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetNotebookTaskStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        notebook_schedule_preview_url: str = None,
        progress: str = None,
        result: str = None,
        status: str = None,
    ):
        self.notebook_schedule_preview_url = notebook_schedule_preview_url
        self.progress = progress
        self.result = result
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notebook_schedule_preview_url is not None:
            result['NotebookSchedulePreviewUrl'] = self.notebook_schedule_preview_url
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotebookSchedulePreviewUrl') is not None:
            self.notebook_schedule_preview_url = m.get('NotebookSchedulePreviewUrl')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetNotebookTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetNotebookTaskStatusResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetNotebookTaskStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNotebookTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNotebookTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNotebookTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAirflowsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_index: int = None,
        skip: int = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.page_index = page_index
        self.skip = skip
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListAirflowsResponseBodyRootList(TeaModel):
    def __init__(
        self,
        airflow_id: str = None,
        airflow_name: str = None,
        app_spec: str = None,
        app_type: str = None,
        custom_airflow_cfg: List[str] = None,
        dags_dir: str = None,
        deploy_error_msg: str = None,
        description: str = None,
        gmt_created: str = None,
        oss_bucket_name: str = None,
        oss_path: str = None,
        plugins_dir: str = None,
        requirement_file: str = None,
        security_group_id: str = None,
        startup_file: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        self.airflow_id = airflow_id
        self.airflow_name = airflow_name
        self.app_spec = app_spec
        self.app_type = app_type
        self.custom_airflow_cfg = custom_airflow_cfg
        self.dags_dir = dags_dir
        self.deploy_error_msg = deploy_error_msg
        self.description = description
        self.gmt_created = gmt_created
        self.oss_bucket_name = oss_bucket_name
        self.oss_path = oss_path
        self.plugins_dir = plugins_dir
        self.requirement_file = requirement_file
        self.security_group_id = security_group_id
        self.startup_file = startup_file
        self.status = status
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id
        self.worker_serverless_replicas = worker_serverless_replicas
        self.workspace_id = workspace_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id
        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name
        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.custom_airflow_cfg is not None:
            result['CustomAirflowCfg'] = self.custom_airflow_cfg
        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir
        if self.deploy_error_msg is not None:
            result['DeployErrorMsg'] = self.deploy_error_msg
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir
        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.worker_serverless_replicas is not None:
            result['WorkerServerlessReplicas'] = self.worker_serverless_replicas
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')
        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')
        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CustomAirflowCfg') is not None:
            self.custom_airflow_cfg = m.get('CustomAirflowCfg')
        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')
        if m.get('DeployErrorMsg') is not None:
            self.deploy_error_msg = m.get('DeployErrorMsg')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')
        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkerServerlessReplicas') is not None:
            self.worker_serverless_replicas = m.get('WorkerServerlessReplicas')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListAirflowsResponseBodyRoot(TeaModel):
    def __init__(
        self,
        list: List[ListAirflowsResponseBodyRootList] = None,
        total_count: int = None,
    ):
        self.list = list
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListAirflowsResponseBodyRootList()
                self.list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAirflowsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_code: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        root: ListAirflowsResponseBodyRoot = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Reuqest ID。
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            temp_model = ListAirflowsResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAirflowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAirflowsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAirflowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakeCatalogRequest(TeaModel):
    def __init__(
        self,
        search_key: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        self.search_key = search_key
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakeCatalogResponseBody(TeaModel):
    def __init__(
        self,
        cata_log_list: List[DLCatalog] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.cata_log_list = cata_log_list
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.cata_log_list:
            for k in self.cata_log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CataLogList'] = []
        if self.cata_log_list is not None:
            for k in self.cata_log_list:
                result['CataLogList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cata_log_list = []
        if m.get('CataLogList') is not None:
            for k in m.get('CataLogList'):
                temp_model = DLCatalog()
                self.cata_log_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLakeCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakeCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakeCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakeDatabaseRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        max_results: int = None,
        next_token: str = None,
        search_key: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        self.max_results = max_results
        self.next_token = next_token
        self.search_key = search_key
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakeDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        database_list: List[DLDatabase] = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.database_list = database_list
        self.error_code = error_code
        self.error_message = error_message
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.database_list:
            for k in self.database_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatabaseList'] = []
        if self.database_list is not None:
            for k in self.database_list:
                result['DatabaseList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_list = []
        if m.get('DatabaseList') is not None:
            for k in m.get('DatabaseList'):
                temp_model = DLDatabase()
                self.database_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLakeDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakeDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakeDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakeFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_name_pattern: str = None,
        max_results: int = None,
        next_token: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        self.db_name = db_name
        self.function_name_pattern = function_name_pattern
        self.max_results = max_results
        self.next_token = next_token
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_name_pattern is not None:
            result['FunctionNamePattern'] = self.function_name_pattern
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionNamePattern') is not None:
            self.function_name_pattern = m.get('FunctionNamePattern')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakeFunctionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        function_list: List[DLFunction] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.function_list = function_list
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.function_list:
            for k in self.function_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['FunctionList'] = []
        if self.function_list is not None:
            for k in self.function_list:
                result['FunctionList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        self.function_list = []
        if m.get('FunctionList') is not None:
            for k in m.get('FunctionList'):
                temp_model = DLFunction()
                self.function_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLakeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakeFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakeFunctionNameRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_name_pattern: str = None,
        max_results: int = None,
        next_token: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.function_name_pattern = function_name_pattern
        self.max_results = max_results
        self.next_token = next_token
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_name_pattern is not None:
            result['FunctionNamePattern'] = self.function_name_pattern
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionNamePattern') is not None:
            self.function_name_pattern = m.get('FunctionNamePattern')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakeFunctionNameResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        function_name_list: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.function_name_list = function_name_list
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.function_name_list is not None:
            result['FunctionNameList'] = self.function_name_list
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('FunctionNameList') is not None:
            self.function_name_list = m.get('FunctionNameList')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLakeFunctionNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakeFunctionNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakeFunctionNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakePartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        max_results: int = None,
        next_token: str = None,
        part_names: List[str] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.max_results = max_results
        self.next_token = next_token
        self.part_names = part_names
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.part_names is not None:
            result['PartNames'] = self.part_names
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PartNames') is not None:
            self.part_names = m.get('PartNames')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakePartitionShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        max_results: int = None,
        next_token: str = None,
        part_names_shrink: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.max_results = max_results
        self.next_token = next_token
        self.part_names_shrink = part_names_shrink
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.part_names_shrink is not None:
            result['PartNames'] = self.part_names_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PartNames') is not None:
            self.part_names_shrink = m.get('PartNames')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakePartitionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        partition_list: List[DLPartition] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.max_results = max_results
        self.next_token = next_token
        self.partition_list = partition_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_list:
            for k in self.partition_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PartitionList'] = []
        if self.partition_list is not None:
            for k in self.partition_list:
                result['PartitionList'].append(k.to_map() if k else None)
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.partition_list = []
        if m.get('PartitionList') is not None:
            for k in m.get('PartitionList'):
                temp_model = DLPartition()
                self.partition_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLakePartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakePartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakePartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakePartitionByFilterRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakePartitionByFilterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        partition_list: List[DLPartition] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.max_results = max_results
        self.next_token = next_token
        self.partition_list = partition_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_list:
            for k in self.partition_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PartitionList'] = []
        if self.partition_list is not None:
            for k in self.partition_list:
                result['PartitionList'].append(k.to_map() if k else None)
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.partition_list = []
        if m.get('PartitionList') is not None:
            for k in m.get('PartitionList'):
                temp_model = DLPartition()
                self.partition_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLakePartitionByFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakePartitionByFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakePartitionByFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakePartitionNameRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        max_results: int = None,
        next_token: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakePartitionNameResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        partition_name_list: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.max_results = max_results
        self.next_token = next_token
        self.partition_name_list = partition_name_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.partition_name_list is not None:
            result['PartitionNameList'] = self.partition_name_list
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PartitionNameList') is not None:
            self.partition_name_list = m.get('PartitionNameList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLakePartitionNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakePartitionNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakePartitionNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakeTableRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        max_results: int = None,
        next_token: str = None,
        table_name_pattern: str = None,
        table_type: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.max_results = max_results
        self.next_token = next_token
        self.table_name_pattern = table_name_pattern
        self.table_type = table_type
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.table_name_pattern is not None:
            result['TableNamePattern'] = self.table_name_pattern
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TableNamePattern') is not None:
            self.table_name_pattern = m.get('TableNamePattern')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakeTableResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        table_list: List[DLTable] = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.table_list = table_list

    def validate(self):
        if self.table_list:
            for k in self.table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TableList'] = []
        if self.table_list is not None:
            for k in self.table_list:
                result['TableList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.table_list = []
        if m.get('TableList') is not None:
            for k in m.get('TableList'):
                temp_model = DLTable()
                self.table_list.append(temp_model.from_map(k))
        return self


class ListDataLakeTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakeTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakeTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakeTableNameRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        max_results: int = None,
        next_token: str = None,
        table_name_pattern: str = None,
        table_type: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.max_results = max_results
        self.next_token = next_token
        self.table_name_pattern = table_name_pattern
        self.table_type = table_type
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.table_name_pattern is not None:
            result['TableNamePattern'] = self.table_name_pattern
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TableNamePattern') is not None:
            self.table_name_pattern = m.get('TableNamePattern')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakeTableNameResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        table_name_list: List[str] = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.table_name_list = table_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table_name_list is not None:
            result['TableNameList'] = self.table_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableNameList') is not None:
            self.table_name_list = m.get('TableNameList')
        return self


class ListDataLakeTableNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakeTableNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakeTableNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLakeTablebaseInfoRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        page: int = None,
        rows: int = None,
        search_key: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.page = page
        self.rows = rows
        self.search_key = search_key
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.page is not None:
            result['Page'] = self.page
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataLakeTablebaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        tablebase_info_list: List[DLTablebaseInfo] = None,
        total_count: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.tablebase_info_list = tablebase_info_list
        self.total_count = total_count

    def validate(self):
        if self.tablebase_info_list:
            for k in self.tablebase_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TablebaseInfoList'] = []
        if self.tablebase_info_list is not None:
            for k in self.tablebase_info_list:
                result['TablebaseInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tablebase_info_list = []
        if m.get('TablebaseInfoList') is not None:
            for k in m.get('TablebaseInfoList'):
                temp_model = DLTablebaseInfo()
                self.tablebase_info_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDataLakeTablebaseInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLakeTablebaseInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataLakeTablebaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendChatMessageRequestDataSource(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_type: str = None,
        database: str = None,
        db_name: str = None,
        dms_database_id: str = None,
        dms_instance_id: str = None,
        engine: str = None,
        file_id: str = None,
        location: str = None,
        region_id: str = None,
        tables: List[str] = None,
    ):
        self.data_source_id = data_source_id
        self.data_source_type = data_source_type
        self.database = database
        self.db_name = db_name
        self.dms_database_id = dms_database_id
        self.dms_instance_id = dms_instance_id
        self.engine = engine
        self.file_id = file_id
        self.location = location
        self.region_id = region_id
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.database is not None:
            result['Database'] = self.database
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.dms_database_id is not None:
            result['DmsDatabaseId'] = self.dms_database_id
        if self.dms_instance_id is not None:
            result['DmsInstanceId'] = self.dms_instance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.location is not None:
            result['Location'] = self.location
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DmsDatabaseId') is not None:
            self.dms_database_id = m.get('DmsDatabaseId')
        if m.get('DmsInstanceId') is not None:
            self.dms_instance_id = m.get('DmsInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class SendChatMessageRequestSessionConfig(TeaModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        custom_agent_stage: str = None,
        language: str = None,
    ):
        self.custom_agent_id = custom_agent_id
        self.custom_agent_stage = custom_agent_stage
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id
        if self.custom_agent_stage is not None:
            result['CustomAgentStage'] = self.custom_agent_stage
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')
        if m.get('CustomAgentStage') is not None:
            self.custom_agent_stage = m.get('CustomAgentStage')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class SendChatMessageRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        dmsunit: str = None,
        data_source: SendChatMessageRequestDataSource = None,
        message: str = None,
        message_type: str = None,
        question: str = None,
        quoted_message: str = None,
        reply_to: str = None,
        session_config: SendChatMessageRequestSessionConfig = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        self.dmsunit = dmsunit
        self.data_source = data_source
        # This parameter is required.
        self.message = message
        self.message_type = message_type
        self.question = question
        self.quoted_message = quoted_message
        self.reply_to = reply_to
        self.session_config = session_config
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.session_config:
            self.session_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.question is not None:
            result['Question'] = self.question
        if self.quoted_message is not None:
            result['QuotedMessage'] = self.quoted_message
        if self.reply_to is not None:
            result['ReplyTo'] = self.reply_to
        if self.session_config is not None:
            result['SessionConfig'] = self.session_config.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')
        if m.get('DataSource') is not None:
            temp_model = SendChatMessageRequestDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('QuotedMessage') is not None:
            self.quoted_message = m.get('QuotedMessage')
        if m.get('ReplyTo') is not None:
            self.reply_to = m.get('ReplyTo')
        if m.get('SessionConfig') is not None:
            temp_model = SendChatMessageRequestSessionConfig()
            self.session_config = temp_model.from_map(m['SessionConfig'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SendChatMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        dmsunit: str = None,
        data_source_shrink: str = None,
        message: str = None,
        message_type: str = None,
        question: str = None,
        quoted_message: str = None,
        reply_to: str = None,
        session_config_shrink: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        self.dmsunit = dmsunit
        self.data_source_shrink = data_source_shrink
        # This parameter is required.
        self.message = message
        self.message_type = message_type
        self.question = question
        self.quoted_message = quoted_message
        self.reply_to = reply_to
        self.session_config_shrink = session_config_shrink
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit
        if self.data_source_shrink is not None:
            result['DataSource'] = self.data_source_shrink
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.question is not None:
            result['Question'] = self.question
        if self.quoted_message is not None:
            result['QuotedMessage'] = self.quoted_message
        if self.reply_to is not None:
            result['ReplyTo'] = self.reply_to
        if self.session_config_shrink is not None:
            result['SessionConfig'] = self.session_config_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')
        if m.get('DataSource') is not None:
            self.data_source_shrink = m.get('DataSource')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('QuotedMessage') is not None:
            self.quoted_message = m.get('QuotedMessage')
        if m.get('ReplyTo') is not None:
            self.reply_to = m.get('ReplyTo')
        if m.get('SessionConfig') is not None:
            self.session_config_shrink = m.get('SessionConfig')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SendChatMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        message: str = None,
        session_id: str = None,
    ):
        # AgentId
        self.agent_id = agent_id
        # Message
        self.message = message
        # SessionId
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.message is not None:
            result['Message'] = self.message
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SendChatMessageResponseBody(TeaModel):
    def __init__(
        self,
        data: SendChatMessageResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SendChatMessageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendChatMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendChatMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendChatMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAirflowRequest(TeaModel):
    def __init__(
        self,
        airflow_id: str = None,
        airflow_name: str = None,
        app_spec: str = None,
        client_token: str = None,
        dags_dir: str = None,
        description: str = None,
        plugins_dir: str = None,
        requirement_file: str = None,
        startup_file: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.airflow_id = airflow_id
        self.airflow_name = airflow_name
        self.app_spec = app_spec
        self.client_token = client_token
        self.dags_dir = dags_dir
        self.description = description
        self.plugins_dir = plugins_dir
        self.requirement_file = requirement_file
        self.startup_file = startup_file
        self.worker_serverless_replicas = worker_serverless_replicas
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id
        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name
        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir
        if self.description is not None:
            result['Description'] = self.description
        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir
        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file
        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file
        if self.worker_serverless_replicas is not None:
            result['WorkerServerlessReplicas'] = self.worker_serverless_replicas
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')
        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')
        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')
        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')
        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')
        if m.get('WorkerServerlessReplicas') is not None:
            self.worker_serverless_replicas = m.get('WorkerServerlessReplicas')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateAirflowResponseBodyRoot(TeaModel):
    def __init__(
        self,
        airflow_name: str = None,
        app_spec: str = None,
        app_type: str = None,
        custom_airflow_cfg: List[str] = None,
        dags_dir: str = None,
        deploy_error_msg: str = None,
        description: str = None,
        environments: str = None,
        gmt_created: str = None,
        oss_bucket_name: str = None,
        oss_path: str = None,
        plugins_dir: str = None,
        requirement_file: str = None,
        requirements: str = None,
        security_group_id: str = None,
        startup_file: str = None,
        status: str = None,
        uuid: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        self.airflow_name = airflow_name
        # SMALL。
        self.app_spec = app_spec
        self.app_type = app_type
        self.custom_airflow_cfg = custom_airflow_cfg
        self.dags_dir = dags_dir
        self.deploy_error_msg = deploy_error_msg
        self.description = description
        self.environments = environments
        self.gmt_created = gmt_created
        self.oss_bucket_name = oss_bucket_name
        self.oss_path = oss_path
        self.plugins_dir = plugins_dir
        self.requirement_file = requirement_file
        self.requirements = requirements
        self.security_group_id = security_group_id
        self.startup_file = startup_file
        self.status = status
        self.uuid = uuid
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id
        self.worker_serverless_replicas = worker_serverless_replicas
        self.workspace_id = workspace_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name
        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.custom_airflow_cfg is not None:
            result['CustomAirflowCfg'] = self.custom_airflow_cfg
        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir
        if self.deploy_error_msg is not None:
            result['DeployErrorMsg'] = self.deploy_error_msg
        if self.description is not None:
            result['Description'] = self.description
        if self.environments is not None:
            result['Environments'] = self.environments
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir
        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file
        if self.requirements is not None:
            result['Requirements'] = self.requirements
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file
        if self.status is not None:
            result['Status'] = self.status
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.worker_serverless_replicas is not None:
            result['WorkerServerlessReplicas'] = self.worker_serverless_replicas
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')
        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CustomAirflowCfg') is not None:
            self.custom_airflow_cfg = m.get('CustomAirflowCfg')
        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')
        if m.get('DeployErrorMsg') is not None:
            self.deploy_error_msg = m.get('DeployErrorMsg')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environments') is not None:
            self.environments = m.get('Environments')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')
        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')
        if m.get('Requirements') is not None:
            self.requirements = m.get('Requirements')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkerServerlessReplicas') is not None:
            self.worker_serverless_replicas = m.get('WorkerServerlessReplicas')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateAirflowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        root: UpdateAirflowResponseBodyRoot = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            temp_model = UpdateAirflowResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAirflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAirflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAirflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataLakeDatabaseRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        description: str = None,
        location: str = None,
        parameters: Dict[str, str] = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.description = description
        # This parameter is required.
        self.location = location
        self.parameters = parameters
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDataLakeDatabaseShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        description: str = None,
        location: str = None,
        parameters_shrink: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        self.description = description
        # This parameter is required.
        self.location = location
        self.parameters_shrink = parameters_shrink
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDataLakeDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        database: DLDatabase = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.database = database
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = DLDatabase()
            self.database = temp_model.from_map(m['Database'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataLakeDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataLakeDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDataLakeDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataLakeFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_input: DLFunctionInput = None,
        function_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.function_input = function_input
        # This parameter is required.
        self.function_name = function_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.function_input:
            self.function_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_input is not None:
            result['FunctionInput'] = self.function_input.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionInput') is not None:
            temp_model = DLFunctionInput()
            self.function_input = temp_model.from_map(m['FunctionInput'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDataLakeFunctionShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_input_shrink: str = None,
        function_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.function_input_shrink = function_input_shrink
        # This parameter is required.
        self.function_name = function_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.function_input_shrink is not None:
            result['FunctionInput'] = self.function_input_shrink
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FunctionInput') is not None:
            self.function_input_shrink = m.get('FunctionInput')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDataLakeFunctionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        function: DLFunction = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.function = function
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.function is not None:
            result['Function'] = self.function.to_map()
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
        if m.get('Function') is not None:
            temp_model = DLFunction()
            self.function = temp_model.from_map(m['Function'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataLakeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataLakeFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDataLakeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataLakePartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        partition_input: DLPartitionInput = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.partition_input = partition_input
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.partition_input:
            self.partition_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.partition_input is not None:
            result['PartitionInput'] = self.partition_input.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('PartitionInput') is not None:
            temp_model = DLPartitionInput()
            self.partition_input = temp_model.from_map(m['PartitionInput'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDataLakePartitionShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        partition_input_shrink: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.partition_input_shrink = partition_input_shrink
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.partition_input_shrink is not None:
            result['PartitionInput'] = self.partition_input_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('PartitionInput') is not None:
            self.partition_input_shrink = m.get('PartitionInput')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDataLakePartitionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataLakePartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataLakePartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDataLakePartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataLakeTableRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        table_input: DLTableInput = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.table_input = table_input
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.table_input:
            self.table_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_input is not None:
            result['TableInput'] = self.table_input.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableInput') is not None:
            temp_model = DLTableInput()
            self.table_input = temp_model.from_map(m['TableInput'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDataLakeTableShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        table_input_shrink: str = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.table_input_shrink = table_input_shrink
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_input_shrink is not None:
            result['TableInput'] = self.table_input_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableInput') is not None:
            self.table_input_shrink = m.get('TableInput')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDataLakeTableResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        table: DLTable = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.table = table

    def validate(self):
        if self.table:
            self.table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table is not None:
            result['Table'] = self.table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Table') is not None:
            temp_model = DLTable()
            self.table = temp_model.from_map(m['Table'])
        return self


class UpdateDataLakeTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataLakeTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDataLakeTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


