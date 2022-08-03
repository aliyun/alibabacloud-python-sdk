# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, BinaryIO


class AccessControlList(TeaModel):
    def __init__(
        self,
        grant: str = None,
    ):
        self.grant = grant

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant is not None:
            result['Grant'] = self.grant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grant') is not None:
            self.grant = m.get('Grant')
        return self


class Owner(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
    ):
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['ID'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        return self


class AccessControlPolicy(TeaModel):
    def __init__(
        self,
        access_control_list: AccessControlList = None,
        owner: Owner = None,
    ):
        self.access_control_list = access_control_list
        self.owner = owner

    def validate(self):
        if self.access_control_list:
            self.access_control_list.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list is not None:
            result['AccessControlList'] = self.access_control_list.to_map()
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlList') is not None:
            temp_model = AccessControlList()
            self.access_control_list = temp_model.from_map(m['AccessControlList'])
        if m.get('Owner') is not None:
            temp_model = Owner()
            self.owner = temp_model.from_map(m['Owner'])
        return self


class ApplyServerSideEncryptionByDefault(TeaModel):
    def __init__(
        self,
        kmsdata_encryption: str = None,
        kmsmaster_key_id: str = None,
        ssealgorithm: str = None,
    ):
        self.kmsdata_encryption = kmsdata_encryption
        self.kmsmaster_key_id = kmsmaster_key_id
        self.ssealgorithm = ssealgorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kmsdata_encryption is not None:
            result['KMSDataEncryption'] = self.kmsdata_encryption
        if self.kmsmaster_key_id is not None:
            result['KMSMasterKeyID'] = self.kmsmaster_key_id
        if self.ssealgorithm is not None:
            result['SSEAlgorithm'] = self.ssealgorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KMSDataEncryption') is not None:
            self.kmsdata_encryption = m.get('KMSDataEncryption')
        if m.get('KMSMasterKeyID') is not None:
            self.kmsmaster_key_id = m.get('KMSMasterKeyID')
        if m.get('SSEAlgorithm') is not None:
            self.ssealgorithm = m.get('SSEAlgorithm')
        return self


class Bucket(TeaModel):
    def __init__(
        self,
        creation_date: str = None,
        extranet_endpoint: str = None,
        intranet_endpoint: str = None,
        location: str = None,
        name: str = None,
        region: str = None,
        storage_class: str = None,
    ):
        self.creation_date = creation_date
        self.extranet_endpoint = extranet_endpoint
        self.intranet_endpoint = intranet_endpoint
        self.location = location
        self.name = name
        self.region = region
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.extranet_endpoint is not None:
            result['ExtranetEndpoint'] = self.extranet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('ExtranetEndpoint') is not None:
            self.extranet_endpoint = m.get('ExtranetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class LoggingEnabled(TeaModel):
    def __init__(
        self,
        target_bucket: str = None,
        target_prefix: str = None,
    ):
        self.target_bucket = target_bucket
        self.target_prefix = target_prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket
        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')
        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')
        return self


class BucketLoggingStatus(TeaModel):
    def __init__(
        self,
        logging_enabled: LoggingEnabled = None,
    ):
        self.logging_enabled = logging_enabled

    def validate(self):
        if self.logging_enabled:
            self.logging_enabled.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoggingEnabled') is not None:
            temp_model = LoggingEnabled()
            self.logging_enabled = temp_model.from_map(m['LoggingEnabled'])
        return self


class CORSRule(TeaModel):
    def __init__(
        self,
        allowed_header: str = None,
        allowed_method: List[str] = None,
        allowed_origin: List[str] = None,
        expose_header: List[str] = None,
        max_age_seconds: int = None,
    ):
        self.allowed_header = allowed_header
        self.allowed_method = allowed_method
        self.allowed_origin = allowed_origin
        self.expose_header = expose_header
        self.max_age_seconds = max_age_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_header is not None:
            result['AllowedHeader'] = self.allowed_header
        if self.allowed_method is not None:
            result['AllowedMethod'] = self.allowed_method
        if self.allowed_origin is not None:
            result['AllowedOrigin'] = self.allowed_origin
        if self.expose_header is not None:
            result['ExposeHeader'] = self.expose_header
        if self.max_age_seconds is not None:
            result['MaxAgeSeconds'] = self.max_age_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedHeader') is not None:
            self.allowed_header = m.get('AllowedHeader')
        if m.get('AllowedMethod') is not None:
            self.allowed_method = m.get('AllowedMethod')
        if m.get('AllowedOrigin') is not None:
            self.allowed_origin = m.get('AllowedOrigin')
        if m.get('ExposeHeader') is not None:
            self.expose_header = m.get('ExposeHeader')
        if m.get('MaxAgeSeconds') is not None:
            self.max_age_seconds = m.get('MaxAgeSeconds')
        return self


class CORSConfiguration(TeaModel):
    def __init__(
        self,
        corsrule: List[CORSRule] = None,
        response_vary: bool = None,
    ):
        self.corsrule = corsrule
        self.response_vary = response_vary

    def validate(self):
        if self.corsrule:
            for k in self.corsrule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CORSRule'] = []
        if self.corsrule is not None:
            for k in self.corsrule:
                result['CORSRule'].append(k.to_map() if k else None)
        if self.response_vary is not None:
            result['ResponseVary'] = self.response_vary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.corsrule = []
        if m.get('CORSRule') is not None:
            for k in m.get('CORSRule'):
                temp_model = CORSRule()
                self.corsrule.append(temp_model.from_map(k))
        if m.get('ResponseVary') is not None:
            self.response_vary = m.get('ResponseVary')
        return self


class CSVInput(TeaModel):
    def __init__(
        self,
        allow_quoted_record_delimiter: bool = None,
        comment_character: str = None,
        field_delimiter: str = None,
        file_header_info: str = None,
        quote_character: str = None,
        range: str = None,
        record_delimiter: str = None,
    ):
        self.allow_quoted_record_delimiter = allow_quoted_record_delimiter
        self.comment_character = comment_character
        self.field_delimiter = field_delimiter
        self.file_header_info = file_header_info
        self.quote_character = quote_character
        self.range = range
        self.record_delimiter = record_delimiter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_quoted_record_delimiter is not None:
            result['AllowQuotedRecordDelimiter'] = self.allow_quoted_record_delimiter
        if self.comment_character is not None:
            result['CommentCharacter'] = self.comment_character
        if self.field_delimiter is not None:
            result['FieldDelimiter'] = self.field_delimiter
        if self.file_header_info is not None:
            result['FileHeaderInfo'] = self.file_header_info
        if self.quote_character is not None:
            result['QuoteCharacter'] = self.quote_character
        if self.range is not None:
            result['Range'] = self.range
        if self.record_delimiter is not None:
            result['RecordDelimiter'] = self.record_delimiter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowQuotedRecordDelimiter') is not None:
            self.allow_quoted_record_delimiter = m.get('AllowQuotedRecordDelimiter')
        if m.get('CommentCharacter') is not None:
            self.comment_character = m.get('CommentCharacter')
        if m.get('FieldDelimiter') is not None:
            self.field_delimiter = m.get('FieldDelimiter')
        if m.get('FileHeaderInfo') is not None:
            self.file_header_info = m.get('FileHeaderInfo')
        if m.get('QuoteCharacter') is not None:
            self.quote_character = m.get('QuoteCharacter')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        if m.get('RecordDelimiter') is not None:
            self.record_delimiter = m.get('RecordDelimiter')
        return self


class CSVOutput(TeaModel):
    def __init__(
        self,
        field_delimiter: str = None,
        record_delimiter: str = None,
    ):
        self.field_delimiter = field_delimiter
        self.record_delimiter = record_delimiter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_delimiter is not None:
            result['FieldDelimiter'] = self.field_delimiter
        if self.record_delimiter is not None:
            result['RecordDelimiter'] = self.record_delimiter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldDelimiter') is not None:
            self.field_delimiter = m.get('FieldDelimiter')
        if m.get('RecordDelimiter') is not None:
            self.record_delimiter = m.get('RecordDelimiter')
        return self


class CommonPrefix(TeaModel):
    def __init__(
        self,
        prefix: str = None,
    ):
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class Part(TeaModel):
    def __init__(
        self,
        etag: str = None,
        last_modified: str = None,
        part_number: int = None,
        size: int = None,
    ):
        self.etag = etag
        self.last_modified = last_modified
        self.part_number = part_number
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.part_number is not None:
            result['PartNumber'] = self.part_number
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('PartNumber') is not None:
            self.part_number = m.get('PartNumber')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CompleteMultipartUpload(TeaModel):
    def __init__(
        self,
        part: List[Part] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = Part()
                self.part.append(temp_model.from_map(k))
        return self


class CopyObjectResult(TeaModel):
    def __init__(
        self,
        etag: str = None,
        last_modified: str = None,
    ):
        self.etag = etag
        self.last_modified = last_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class CopyPartResult(TeaModel):
    def __init__(
        self,
        etag: str = None,
        last_modified: str = None,
    ):
        self.etag = etag
        self.last_modified = last_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class CreateBucketConfiguration(TeaModel):
    def __init__(
        self,
        data_redundancy_type: str = None,
        storage_class: str = None,
    ):
        self.data_redundancy_type = data_redundancy_type
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class ObjectIdentifier(TeaModel):
    def __init__(
        self,
        key: str = None,
        version_id: str = None,
    ):
        self.key = key
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class Delete(TeaModel):
    def __init__(
        self,
        objects: List[ObjectIdentifier] = None,
        quiet: bool = None,
    ):
        self.objects = objects
        self.quiet = quiet

    def validate(self):
        if self.objects:
            for k in self.objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Object'] = []
        if self.objects is not None:
            for k in self.objects:
                result['Object'].append(k.to_map() if k else None)
        if self.quiet is not None:
            result['Quiet'] = self.quiet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.objects = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ObjectIdentifier()
                self.objects.append(temp_model.from_map(k))
        if m.get('Quiet') is not None:
            self.quiet = m.get('Quiet')
        return self


class DeleteMarkerEntry(TeaModel):
    def __init__(
        self,
        is_latest: bool = None,
        key: str = None,
        last_modified: str = None,
        owner: Owner = None,
        version_id: str = None,
    ):
        self.is_latest = is_latest
        self.key = key
        self.last_modified = last_modified
        self.owner = owner
        self.version_id = version_id

    def validate(self):
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_latest is not None:
            result['IsLatest'] = self.is_latest
        if self.key is not None:
            result['Key'] = self.key
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsLatest') is not None:
            self.is_latest = m.get('IsLatest')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Owner') is not None:
            temp_model = Owner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeletedObject(TeaModel):
    def __init__(
        self,
        delete_marker: bool = None,
        delete_marker_version_id: str = None,
        key: str = None,
        version_id: str = None,
    ):
        self.delete_marker = delete_marker
        self.delete_marker_version_id = delete_marker_version_id
        self.key = key
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_marker is not None:
            result['DeleteMarker'] = self.delete_marker
        if self.delete_marker_version_id is not None:
            result['DeleteMarkerVersionId'] = self.delete_marker_version_id
        if self.key is not None:
            result['Key'] = self.key
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteMarker') is not None:
            self.delete_marker = m.get('DeleteMarker')
        if m.get('DeleteMarkerVersionId') is not None:
            self.delete_marker_version_id = m.get('DeleteMarkerVersionId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class Error(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.host_id = host_id
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ErrorDocument(TeaModel):
    def __init__(
        self,
        http_status: str = None,
        key: str = None,
    ):
        self.http_status = http_status
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ExtendWormConfiguration(TeaModel):
    def __init__(
        self,
        retention_period_in_days: int = None,
    ):
        self.retention_period_in_days = retention_period_in_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.retention_period_in_days is not None:
            result['RetentionPeriodInDays'] = self.retention_period_in_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetentionPeriodInDays') is not None:
            self.retention_period_in_days = m.get('RetentionPeriodInDays')
        return self


class IndexDocument(TeaModel):
    def __init__(
        self,
        suffix: str = None,
        support_sub_dir: bool = None,
        type: str = None,
    ):
        self.suffix = suffix
        self.support_sub_dir = support_sub_dir
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.suffix is not None:
            result['Suffix'] = self.suffix
        if self.support_sub_dir is not None:
            result['SupportSubDir'] = self.support_sub_dir
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')
        if m.get('SupportSubDir') is not None:
            self.support_sub_dir = m.get('SupportSubDir')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InitiateWormConfiguration(TeaModel):
    def __init__(
        self,
        retention_period_in_days: int = None,
    ):
        self.retention_period_in_days = retention_period_in_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.retention_period_in_days is not None:
            result['RetentionPeriodInDays'] = self.retention_period_in_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetentionPeriodInDays') is not None:
            self.retention_period_in_days = m.get('RetentionPeriodInDays')
        return self


class JSONInput(TeaModel):
    def __init__(
        self,
        parse_json_number_as_string: bool = None,
        range: str = None,
        type: str = None,
    ):
        self.parse_json_number_as_string = parse_json_number_as_string
        self.range = range
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parse_json_number_as_string is not None:
            result['ParseJsonNumberAsString'] = self.parse_json_number_as_string
        if self.range is not None:
            result['Range'] = self.range
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParseJsonNumberAsString') is not None:
            self.parse_json_number_as_string = m.get('ParseJsonNumberAsString')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InputSerialization(TeaModel):
    def __init__(
        self,
        csv: CSVInput = None,
        compression_type: str = None,
        json: JSONInput = None,
    ):
        self.csv = csv
        self.compression_type = compression_type
        self.json = json

    def validate(self):
        if self.csv:
            self.csv.validate()
        if self.json:
            self.json.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csv is not None:
            result['CSV'] = self.csv.to_map()
        if self.compression_type is not None:
            result['CompressionType'] = self.compression_type
        if self.json is not None:
            result['JSON'] = self.json.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CSV') is not None:
            temp_model = CSVInput()
            self.csv = temp_model.from_map(m['CSV'])
        if m.get('CompressionType') is not None:
            self.compression_type = m.get('CompressionType')
        if m.get('JSON') is not None:
            temp_model = JSONInput()
            self.json = temp_model.from_map(m['JSON'])
        return self


class InventoryConfigurationOptionalFields(TeaModel):
    def __init__(
        self,
        fields: List[str] = None,
    ):
        self.fields = fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Field'] = self.fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.fields = m.get('Field')
        return self


class SSEKMS(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class SSEOSS(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class InventoryEncryption(TeaModel):
    def __init__(
        self,
        ssekms: SSEKMS = None,
        sseoss: SSEOSS = None,
    ):
        self.ssekms = ssekms
        self.sseoss = sseoss

    def validate(self):
        if self.ssekms:
            self.ssekms.validate()
        if self.sseoss:
            self.sseoss.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ssekms is not None:
            result['SSE-KMS'] = self.ssekms.to_map()
        if self.sseoss is not None:
            result['SSE-OSS'] = self.sseoss.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SSE-KMS') is not None:
            temp_model = SSEKMS()
            self.ssekms = temp_model.from_map(m['SSE-KMS'])
        if m.get('SSE-OSS') is not None:
            temp_model = SSEOSS()
            self.sseoss = temp_model.from_map(m['SSE-OSS'])
        return self


class InventoryOSSBucketDestination(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        bucket: str = None,
        encryption: InventoryEncryption = None,
        format: str = None,
        prefix: str = None,
        role_arn: str = None,
    ):
        self.account_id = account_id
        self.bucket = bucket
        self.encryption = encryption
        self.format = format
        self.prefix = prefix
        self.role_arn = role_arn

    def validate(self):
        if self.encryption:
            self.encryption.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.encryption is not None:
            result['Encryption'] = self.encryption.to_map()
        if self.format is not None:
            result['Format'] = self.format
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Encryption') is not None:
            temp_model = InventoryEncryption()
            self.encryption = temp_model.from_map(m['Encryption'])
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class InventoryDestination(TeaModel):
    def __init__(
        self,
        ossbucket_destination: InventoryOSSBucketDestination = None,
    ):
        self.ossbucket_destination = ossbucket_destination

    def validate(self):
        if self.ossbucket_destination:
            self.ossbucket_destination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ossbucket_destination is not None:
            result['OSSBucketDestination'] = self.ossbucket_destination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucketDestination') is not None:
            temp_model = InventoryOSSBucketDestination()
            self.ossbucket_destination = temp_model.from_map(m['OSSBucketDestination'])
        return self


class InventoryFilter(TeaModel):
    def __init__(
        self,
        prefix: str = None,
    ):
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class InventorySchedule(TeaModel):
    def __init__(
        self,
        frequency: str = None,
    ):
        self.frequency = frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        return self


class InventoryConfiguration(TeaModel):
    def __init__(
        self,
        destination: InventoryDestination = None,
        filter: InventoryFilter = None,
        id: str = None,
        included_object_versions: str = None,
        is_enabled: bool = None,
        optional_fields: InventoryConfigurationOptionalFields = None,
        schedule: InventorySchedule = None,
    ):
        self.destination = destination
        self.filter = filter
        self.id = id
        self.included_object_versions = included_object_versions
        self.is_enabled = is_enabled
        self.optional_fields = optional_fields
        self.schedule = schedule

    def validate(self):
        if self.destination:
            self.destination.validate()
        if self.filter:
            self.filter.validate()
        if self.optional_fields:
            self.optional_fields.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.included_object_versions is not None:
            result['IncludedObjectVersions'] = self.included_object_versions
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.optional_fields is not None:
            result['OptionalFields'] = self.optional_fields.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            temp_model = InventoryDestination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('Filter') is not None:
            temp_model = InventoryFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludedObjectVersions') is not None:
            self.included_object_versions = m.get('IncludedObjectVersions')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('OptionalFields') is not None:
            temp_model = InventoryConfigurationOptionalFields()
            self.optional_fields = temp_model.from_map(m['OptionalFields'])
        if m.get('Schedule') is not None:
            temp_model = InventorySchedule()
            self.schedule = temp_model.from_map(m['Schedule'])
        return self


class JSONOutput(TeaModel):
    def __init__(
        self,
        record_delimiter: str = None,
    ):
        self.record_delimiter = record_delimiter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_delimiter is not None:
            result['RecordDelimiter'] = self.record_delimiter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordDelimiter') is not None:
            self.record_delimiter = m.get('RecordDelimiter')
        return self


class LifecycleRuleLifecycleAbortMultipartUpload(TeaModel):
    def __init__(
        self,
        created_before_date: str = None,
        days: int = None,
    ):
        self.created_before_date = created_before_date
        self.days = days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_before_date is not None:
            result['CreatedBeforeDate'] = self.created_before_date
        if self.days is not None:
            result['Days'] = self.days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBeforeDate') is not None:
            self.created_before_date = m.get('CreatedBeforeDate')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        return self


class LifecycleRuleLifecycleExpiration(TeaModel):
    def __init__(
        self,
        created_before_date: str = None,
        days: int = None,
        expired_object_delete_marker: bool = None,
    ):
        self.created_before_date = created_before_date
        self.days = days
        self.expired_object_delete_marker = expired_object_delete_marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_before_date is not None:
            result['CreatedBeforeDate'] = self.created_before_date
        if self.days is not None:
            result['Days'] = self.days
        if self.expired_object_delete_marker is not None:
            result['ExpiredObjectDeleteMarker'] = self.expired_object_delete_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBeforeDate') is not None:
            self.created_before_date = m.get('CreatedBeforeDate')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('ExpiredObjectDeleteMarker') is not None:
            self.expired_object_delete_marker = m.get('ExpiredObjectDeleteMarker')
        return self


class LifecycleRuleNoncurrentVersionExpiration(TeaModel):
    def __init__(
        self,
        noncurrent_days: int = None,
    ):
        self.noncurrent_days = noncurrent_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.noncurrent_days is not None:
            result['NoncurrentDays'] = self.noncurrent_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoncurrentDays') is not None:
            self.noncurrent_days = m.get('NoncurrentDays')
        return self


class LifecycleRuleNoncurrentVersionTransition(TeaModel):
    def __init__(
        self,
        noncurrent_days: int = None,
        storage_class: str = None,
    ):
        self.noncurrent_days = noncurrent_days
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.noncurrent_days is not None:
            result['NoncurrentDays'] = self.noncurrent_days
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoncurrentDays') is not None:
            self.noncurrent_days = m.get('NoncurrentDays')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class LifecycleRuleTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class LifecycleRuleLifecycleTransition(TeaModel):
    def __init__(
        self,
        created_before_date: str = None,
        days: int = None,
        storage_class: str = None,
    ):
        self.created_before_date = created_before_date
        self.days = days
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_before_date is not None:
            result['CreatedBeforeDate'] = self.created_before_date
        if self.days is not None:
            result['Days'] = self.days
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBeforeDate') is not None:
            self.created_before_date = m.get('CreatedBeforeDate')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class LifecycleRule(TeaModel):
    def __init__(
        self,
        lifecycle_abort_multipart_upload: LifecycleRuleLifecycleAbortMultipartUpload = None,
        lifecycle_expiration: LifecycleRuleLifecycleExpiration = None,
        id: str = None,
        noncurrent_version_expiration: LifecycleRuleNoncurrentVersionExpiration = None,
        noncurrent_version_transition: List[LifecycleRuleNoncurrentVersionTransition] = None,
        prefix: str = None,
        status: str = None,
        tag: List[LifecycleRuleTag] = None,
        lifecycle_transition: List[LifecycleRuleLifecycleTransition] = None,
    ):
        self.lifecycle_abort_multipart_upload = lifecycle_abort_multipart_upload
        self.lifecycle_expiration = lifecycle_expiration
        self.id = id
        self.noncurrent_version_expiration = noncurrent_version_expiration
        self.noncurrent_version_transition = noncurrent_version_transition
        self.prefix = prefix
        self.status = status
        self.tag = tag
        self.lifecycle_transition = lifecycle_transition

    def validate(self):
        if self.lifecycle_abort_multipart_upload:
            self.lifecycle_abort_multipart_upload.validate()
        if self.lifecycle_expiration:
            self.lifecycle_expiration.validate()
        if self.noncurrent_version_expiration:
            self.noncurrent_version_expiration.validate()
        if self.noncurrent_version_transition:
            for k in self.noncurrent_version_transition:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.lifecycle_transition:
            for k in self.lifecycle_transition:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle_abort_multipart_upload is not None:
            result['AbortMultipartUpload'] = self.lifecycle_abort_multipart_upload.to_map()
        if self.lifecycle_expiration is not None:
            result['Expiration'] = self.lifecycle_expiration.to_map()
        if self.id is not None:
            result['ID'] = self.id
        if self.noncurrent_version_expiration is not None:
            result['NoncurrentVersionExpiration'] = self.noncurrent_version_expiration.to_map()
        result['NoncurrentVersionTransition'] = []
        if self.noncurrent_version_transition is not None:
            for k in self.noncurrent_version_transition:
                result['NoncurrentVersionTransition'].append(k.to_map() if k else None)
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['Transition'] = []
        if self.lifecycle_transition is not None:
            for k in self.lifecycle_transition:
                result['Transition'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbortMultipartUpload') is not None:
            temp_model = LifecycleRuleLifecycleAbortMultipartUpload()
            self.lifecycle_abort_multipart_upload = temp_model.from_map(m['AbortMultipartUpload'])
        if m.get('Expiration') is not None:
            temp_model = LifecycleRuleLifecycleExpiration()
            self.lifecycle_expiration = temp_model.from_map(m['Expiration'])
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('NoncurrentVersionExpiration') is not None:
            temp_model = LifecycleRuleNoncurrentVersionExpiration()
            self.noncurrent_version_expiration = temp_model.from_map(m['NoncurrentVersionExpiration'])
        self.noncurrent_version_transition = []
        if m.get('NoncurrentVersionTransition') is not None:
            for k in m.get('NoncurrentVersionTransition'):
                temp_model = LifecycleRuleNoncurrentVersionTransition()
                self.noncurrent_version_transition.append(temp_model.from_map(k))
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = LifecycleRuleTag()
                self.tag.append(temp_model.from_map(k))
        self.lifecycle_transition = []
        if m.get('Transition') is not None:
            for k in m.get('Transition'):
                temp_model = LifecycleRuleLifecycleTransition()
                self.lifecycle_transition.append(temp_model.from_map(k))
        return self


class LifecycleConfiguration(TeaModel):
    def __init__(
        self,
        rule: List[LifecycleRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = LifecycleRule()
                self.rule.append(temp_model.from_map(k))
        return self


class LiveChannelPlayUrls(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class LiveChannelPublishUrls(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class LiveChannel(TeaModel):
    def __init__(
        self,
        description: str = None,
        last_modified: str = None,
        name: str = None,
        play_urls: LiveChannelPlayUrls = None,
        publish_urls: LiveChannelPublishUrls = None,
        status: str = None,
    ):
        self.description = description
        self.last_modified = last_modified
        self.name = name
        self.play_urls = play_urls
        self.publish_urls = publish_urls
        self.status = status

    def validate(self):
        if self.play_urls:
            self.play_urls.validate()
        if self.publish_urls:
            self.publish_urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.play_urls is not None:
            result['PlayUrls'] = self.play_urls.to_map()
        if self.publish_urls is not None:
            result['PublishUrls'] = self.publish_urls.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlayUrls') is not None:
            temp_model = LiveChannelPlayUrls()
            self.play_urls = temp_model.from_map(m['PlayUrls'])
        if m.get('PublishUrls') is not None:
            temp_model = LiveChannelPublishUrls()
            self.publish_urls = temp_model.from_map(m['PublishUrls'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class LiveChannelAudio(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        codec: str = None,
        sample_rate: int = None,
    ):
        self.bandwidth = bandwidth
        self.codec = codec
        self.sample_rate = sample_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.codec is not None:
            result['Codec'] = self.codec
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        return self


class LiveChannelSnapshot(TeaModel):
    def __init__(
        self,
        dest_bucket: str = None,
        interval: int = None,
        notify_topic: str = None,
        role_name: str = None,
    ):
        self.dest_bucket = dest_bucket
        self.interval = interval
        self.notify_topic = notify_topic
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_bucket is not None:
            result['DestBucket'] = self.dest_bucket
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.notify_topic is not None:
            result['NotifyTopic'] = self.notify_topic
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestBucket') is not None:
            self.dest_bucket = m.get('DestBucket')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('NotifyTopic') is not None:
            self.notify_topic = m.get('NotifyTopic')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class LiveChannelTarget(TeaModel):
    def __init__(
        self,
        frag_count: int = None,
        frag_duration: int = None,
        playlist_name: str = None,
        type: str = None,
    ):
        self.frag_count = frag_count
        self.frag_duration = frag_duration
        self.playlist_name = playlist_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frag_count is not None:
            result['FragCount'] = self.frag_count
        if self.frag_duration is not None:
            result['FragDuration'] = self.frag_duration
        if self.playlist_name is not None:
            result['PlaylistName'] = self.playlist_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FragCount') is not None:
            self.frag_count = m.get('FragCount')
        if m.get('FragDuration') is not None:
            self.frag_duration = m.get('FragDuration')
        if m.get('PlaylistName') is not None:
            self.playlist_name = m.get('PlaylistName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class LiveChannelConfiguration(TeaModel):
    def __init__(
        self,
        description: str = None,
        snapshot: LiveChannelSnapshot = None,
        status: str = None,
        target: LiveChannelTarget = None,
    ):
        self.description = description
        self.snapshot = snapshot
        self.status = status
        self.target = target

    def validate(self):
        if self.snapshot:
            self.snapshot.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Snapshot') is not None:
            temp_model = LiveChannelSnapshot()
            self.snapshot = temp_model.from_map(m['Snapshot'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            temp_model = LiveChannelTarget()
            self.target = temp_model.from_map(m['Target'])
        return self


class LiveChannelVideo(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        codec: str = None,
        frame_rate: int = None,
        height: int = None,
        width: int = None,
    ):
        self.bandwidth = bandwidth
        self.codec = codec
        self.frame_rate = frame_rate
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.codec is not None:
            result['Codec'] = self.codec
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class LiveRecord(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        remote_addr: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.remote_addr = remote_addr
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.remote_addr is not None:
            result['RemoteAddr'] = self.remote_addr
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RemoteAddr') is not None:
            self.remote_addr = m.get('RemoteAddr')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class LocationTransferTypeTransferTypes(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class LocationTransferType(TeaModel):
    def __init__(
        self,
        location: str = None,
        transfer_types: LocationTransferTypeTransferTypes = None,
    ):
        self.location = location
        self.transfer_types = transfer_types

    def validate(self):
        if self.transfer_types:
            self.transfer_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.transfer_types is not None:
            result['TransferTypes'] = self.transfer_types.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('TransferTypes') is not None:
            temp_model = LocationTransferTypeTransferTypes()
            self.transfer_types = temp_model.from_map(m['TransferTypes'])
        return self


class ObjectSummary(TeaModel):
    def __init__(
        self,
        etag: str = None,
        key: str = None,
        last_modified: str = None,
        owner: Owner = None,
        size: int = None,
        storage_class: str = None,
        type: str = None,
    ):
        self.etag = etag
        self.key = key
        self.last_modified = last_modified
        self.owner = owner
        self.size = size
        self.storage_class = storage_class
        self.type = type

    def validate(self):
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.key is not None:
            result['Key'] = self.key
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Owner') is not None:
            temp_model = Owner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ObjectVersion(TeaModel):
    def __init__(
        self,
        etag: str = None,
        is_latest: bool = None,
        key: str = None,
        last_modified: str = None,
        owner: Owner = None,
        size: int = None,
        storage_class: str = None,
        version_id: str = None,
    ):
        self.etag = etag
        self.is_latest = is_latest
        self.key = key
        self.last_modified = last_modified
        self.owner = owner
        self.size = size
        self.storage_class = storage_class
        self.version_id = version_id

    def validate(self):
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.is_latest is not None:
            result['IsLatest'] = self.is_latest
        if self.key is not None:
            result['Key'] = self.key
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('IsLatest') is not None:
            self.is_latest = m.get('IsLatest')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Owner') is not None:
            temp_model = Owner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class OutputSerialization(TeaModel):
    def __init__(
        self,
        csv: CSVOutput = None,
        enable_payload_crc: bool = None,
        json: JSONOutput = None,
        keep_all_columns: bool = None,
        output_header: bool = None,
        output_raw_data: bool = None,
    ):
        self.csv = csv
        self.enable_payload_crc = enable_payload_crc
        self.json = json
        self.keep_all_columns = keep_all_columns
        self.output_header = output_header
        self.output_raw_data = output_raw_data

    def validate(self):
        if self.csv:
            self.csv.validate()
        if self.json:
            self.json.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csv is not None:
            result['CSV'] = self.csv.to_map()
        if self.enable_payload_crc is not None:
            result['EnablePayloadCrc'] = self.enable_payload_crc
        if self.json is not None:
            result['JSON'] = self.json.to_map()
        if self.keep_all_columns is not None:
            result['KeepAllColumns'] = self.keep_all_columns
        if self.output_header is not None:
            result['OutputHeader'] = self.output_header
        if self.output_raw_data is not None:
            result['OutputRawData'] = self.output_raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CSV') is not None:
            temp_model = CSVOutput()
            self.csv = temp_model.from_map(m['CSV'])
        if m.get('EnablePayloadCrc') is not None:
            self.enable_payload_crc = m.get('EnablePayloadCrc')
        if m.get('JSON') is not None:
            temp_model = JSONOutput()
            self.json = temp_model.from_map(m['JSON'])
        if m.get('KeepAllColumns') is not None:
            self.keep_all_columns = m.get('KeepAllColumns')
        if m.get('OutputHeader') is not None:
            self.output_header = m.get('OutputHeader')
        if m.get('OutputRawData') is not None:
            self.output_raw_data = m.get('OutputRawData')
        return self


class RefererConfigurationRefererList(TeaModel):
    def __init__(
        self,
        referer: List[str] = None,
    ):
        self.referer = referer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.referer is not None:
            result['Referer'] = self.referer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        return self


class RefererConfiguration(TeaModel):
    def __init__(
        self,
        allow_empty_referer: bool = None,
        allow_truncate_query_string: bool = None,
        referer_list: RefererConfigurationRefererList = None,
    ):
        self.allow_empty_referer = allow_empty_referer
        self.allow_truncate_query_string = allow_truncate_query_string
        self.referer_list = referer_list

    def validate(self):
        if self.referer_list:
            self.referer_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_empty_referer is not None:
            result['AllowEmptyReferer'] = self.allow_empty_referer
        if self.allow_truncate_query_string is not None:
            result['AllowTruncateQueryString'] = self.allow_truncate_query_string
        if self.referer_list is not None:
            result['RefererList'] = self.referer_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowEmptyReferer') is not None:
            self.allow_empty_referer = m.get('AllowEmptyReferer')
        if m.get('AllowTruncateQueryString') is not None:
            self.allow_truncate_query_string = m.get('AllowTruncateQueryString')
        if m.get('RefererList') is not None:
            temp_model = RefererConfigurationRefererList()
            self.referer_list = temp_model.from_map(m['RefererList'])
        return self


class RegionInfo(TeaModel):
    def __init__(
        self,
        accelerate_endpoint: str = None,
        internal_endpoint: str = None,
        internet_endpoint: str = None,
        region: str = None,
    ):
        self.accelerate_endpoint = accelerate_endpoint
        self.internal_endpoint = internal_endpoint
        self.internet_endpoint = internet_endpoint
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_endpoint is not None:
            result['AccelerateEndpoint'] = self.accelerate_endpoint
        if self.internal_endpoint is not None:
            result['InternalEndpoint'] = self.internal_endpoint
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateEndpoint') is not None:
            self.accelerate_endpoint = m.get('AccelerateEndpoint')
        if m.get('InternalEndpoint') is not None:
            self.internal_endpoint = m.get('InternalEndpoint')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ReplicationDestination(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        transfer_type: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.transfer_type = transfer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.location is not None:
            result['Location'] = self.location
        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')
        return self


class ReplicationPrefixSet(TeaModel):
    def __init__(
        self,
        prefixs: List[str] = None,
    ):
        self.prefixs = prefixs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefixs is not None:
            result['Prefix'] = self.prefixs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prefix') is not None:
            self.prefixs = m.get('Prefix')
        return self


class ReplicationSourceSelectionCriteriaSseKmsEncryptedObjects(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ReplicationSourceSelectionCriteria(TeaModel):
    def __init__(
        self,
        sse_kms_encrypted_objects: ReplicationSourceSelectionCriteriaSseKmsEncryptedObjects = None,
    ):
        self.sse_kms_encrypted_objects = sse_kms_encrypted_objects

    def validate(self):
        if self.sse_kms_encrypted_objects:
            self.sse_kms_encrypted_objects.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sse_kms_encrypted_objects is not None:
            result['SseKmsEncryptedObjects'] = self.sse_kms_encrypted_objects.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SseKmsEncryptedObjects') is not None:
            temp_model = ReplicationSourceSelectionCriteriaSseKmsEncryptedObjects()
            self.sse_kms_encrypted_objects = temp_model.from_map(m['SseKmsEncryptedObjects'])
        return self


class ReplicationRuleEncryptionConfiguration(TeaModel):
    def __init__(
        self,
        replica_kms_key_id: str = None,
    ):
        self.replica_kms_key_id = replica_kms_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.replica_kms_key_id is not None:
            result['ReplicaKmsKeyID'] = self.replica_kms_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReplicaKmsKeyID') is not None:
            self.replica_kms_key_id = m.get('ReplicaKmsKeyID')
        return self


class ReplicationRule(TeaModel):
    def __init__(
        self,
        action: str = None,
        destination: ReplicationDestination = None,
        encryption_configuration: ReplicationRuleEncryptionConfiguration = None,
        historical_object_replication: str = None,
        id: str = None,
        prefix_set: ReplicationPrefixSet = None,
        source_selection_criteria: ReplicationSourceSelectionCriteria = None,
        status: str = None,
        sync_role: str = None,
    ):
        self.action = action
        self.destination = destination
        self.encryption_configuration = encryption_configuration
        self.historical_object_replication = historical_object_replication
        self.id = id
        self.prefix_set = prefix_set
        self.source_selection_criteria = source_selection_criteria
        self.status = status
        self.sync_role = sync_role

    def validate(self):
        if self.destination:
            self.destination.validate()
        if self.encryption_configuration:
            self.encryption_configuration.validate()
        if self.prefix_set:
            self.prefix_set.validate()
        if self.source_selection_criteria:
            self.source_selection_criteria.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.encryption_configuration is not None:
            result['EncryptionConfiguration'] = self.encryption_configuration.to_map()
        if self.historical_object_replication is not None:
            result['HistoricalObjectReplication'] = self.historical_object_replication
        if self.id is not None:
            result['ID'] = self.id
        if self.prefix_set is not None:
            result['PrefixSet'] = self.prefix_set.to_map()
        if self.source_selection_criteria is not None:
            result['SourceSelectionCriteria'] = self.source_selection_criteria.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.sync_role is not None:
            result['SyncRole'] = self.sync_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Destination') is not None:
            temp_model = ReplicationDestination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('EncryptionConfiguration') is not None:
            temp_model = ReplicationRuleEncryptionConfiguration()
            self.encryption_configuration = temp_model.from_map(m['EncryptionConfiguration'])
        if m.get('HistoricalObjectReplication') is not None:
            self.historical_object_replication = m.get('HistoricalObjectReplication')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('PrefixSet') is not None:
            temp_model = ReplicationPrefixSet()
            self.prefix_set = temp_model.from_map(m['PrefixSet'])
        if m.get('SourceSelectionCriteria') is not None:
            temp_model = ReplicationSourceSelectionCriteria()
            self.source_selection_criteria = temp_model.from_map(m['SourceSelectionCriteria'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SyncRole') is not None:
            self.sync_role = m.get('SyncRole')
        return self


class ReplicationConfiguration(TeaModel):
    def __init__(
        self,
        rule: ReplicationRule = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule is not None:
            result['Rule'] = self.rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            temp_model = ReplicationRule()
            self.rule = temp_model.from_map(m['Rule'])
        return self


class ReplicationProgressRuleProgress(TeaModel):
    def __init__(
        self,
        historical_object: str = None,
        new_object: str = None,
    ):
        self.historical_object = historical_object
        self.new_object = new_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.historical_object is not None:
            result['HistoricalObject'] = self.historical_object
        if self.new_object is not None:
            result['NewObject'] = self.new_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoricalObject') is not None:
            self.historical_object = m.get('HistoricalObject')
        if m.get('NewObject') is not None:
            self.new_object = m.get('NewObject')
        return self


class ReplicationProgressRule(TeaModel):
    def __init__(
        self,
        action: str = None,
        destination: ReplicationDestination = None,
        historical_object_replication: str = None,
        id: str = None,
        prefix_set: ReplicationPrefixSet = None,
        progress: ReplicationProgressRuleProgress = None,
        status: str = None,
    ):
        self.action = action
        self.destination = destination
        self.historical_object_replication = historical_object_replication
        self.id = id
        self.prefix_set = prefix_set
        self.progress = progress
        self.status = status

    def validate(self):
        if self.destination:
            self.destination.validate()
        if self.prefix_set:
            self.prefix_set.validate()
        if self.progress:
            self.progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.historical_object_replication is not None:
            result['HistoricalObjectReplication'] = self.historical_object_replication
        if self.id is not None:
            result['ID'] = self.id
        if self.prefix_set is not None:
            result['PrefixSet'] = self.prefix_set.to_map()
        if self.progress is not None:
            result['Progress'] = self.progress.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Destination') is not None:
            temp_model = ReplicationDestination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('HistoricalObjectReplication') is not None:
            self.historical_object_replication = m.get('HistoricalObjectReplication')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('PrefixSet') is not None:
            temp_model = ReplicationPrefixSet()
            self.prefix_set = temp_model.from_map(m['PrefixSet'])
        if m.get('Progress') is not None:
            temp_model = ReplicationProgressRuleProgress()
            self.progress = temp_model.from_map(m['Progress'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ReplicationRuleProgress(TeaModel):
    def __init__(
        self,
        action: str = None,
        id: str = None,
        prefix_set: ReplicationPrefixSet = None,
    ):
        self.action = action
        self.id = id
        self.prefix_set = prefix_set

    def validate(self):
        if self.prefix_set:
            self.prefix_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.id is not None:
            result['ID'] = self.id
        if self.prefix_set is not None:
            result['PrefixSet'] = self.prefix_set.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('PrefixSet') is not None:
            temp_model = ReplicationPrefixSet()
            self.prefix_set = temp_model.from_map(m['PrefixSet'])
        return self


class ReplicationRules(TeaModel):
    def __init__(
        self,
        ids: List[str] = None,
    ):
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ID'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ID') is not None:
            self.ids = m.get('ID')
        return self


class RequestPaymentConfiguration(TeaModel):
    def __init__(
        self,
        payer: str = None,
    ):
        self.payer = payer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payer is not None:
            result['Payer'] = self.payer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        return self


class RestoreRequestJobParameters(TeaModel):
    def __init__(
        self,
        tier: str = None,
    ):
        self.tier = tier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tier is not None:
            result['Tier'] = self.tier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tier') is not None:
            self.tier = m.get('Tier')
        return self


class RestoreRequest(TeaModel):
    def __init__(
        self,
        days: int = None,
        job_parameters: RestoreRequestJobParameters = None,
    ):
        self.days = days
        self.job_parameters = job_parameters

    def validate(self):
        if self.job_parameters:
            self.job_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['Days'] = self.days
        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('JobParameters') is not None:
            temp_model = RestoreRequestJobParameters()
            self.job_parameters = temp_model.from_map(m['JobParameters'])
        return self


class RoutingRuleCondition(TeaModel):
    def __init__(
        self,
        http_error_code_returned_equals: int = None,
        key_prefix_equals: str = None,
    ):
        self.http_error_code_returned_equals = http_error_code_returned_equals
        self.key_prefix_equals = key_prefix_equals

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_error_code_returned_equals is not None:
            result['HttpErrorCodeReturnedEquals'] = self.http_error_code_returned_equals
        if self.key_prefix_equals is not None:
            result['KeyPrefixEquals'] = self.key_prefix_equals
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpErrorCodeReturnedEquals') is not None:
            self.http_error_code_returned_equals = m.get('HttpErrorCodeReturnedEquals')
        if m.get('KeyPrefixEquals') is not None:
            self.key_prefix_equals = m.get('KeyPrefixEquals')
        return self


class RoutingRuleRedirectMirrorHeadersSet(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RoutingRuleRedirectMirrorHeaders(TeaModel):
    def __init__(
        self,
        pass_: List[str] = None,
        pass_all: bool = None,
        remove: List[str] = None,
        set: List[RoutingRuleRedirectMirrorHeadersSet] = None,
    ):
        self.pass_ = pass_
        self.pass_all = pass_all
        self.remove = remove
        self.set = set

    def validate(self):
        if self.set:
            for k in self.set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pass_ is not None:
            result['Pass'] = self.pass_
        if self.pass_all is not None:
            result['PassAll'] = self.pass_all
        if self.remove is not None:
            result['Remove'] = self.remove
        result['Set'] = []
        if self.set is not None:
            for k in self.set:
                result['Set'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')
        if m.get('PassAll') is not None:
            self.pass_all = m.get('PassAll')
        if m.get('Remove') is not None:
            self.remove = m.get('Remove')
        self.set = []
        if m.get('Set') is not None:
            for k in m.get('Set'):
                temp_model = RoutingRuleRedirectMirrorHeadersSet()
                self.set.append(temp_model.from_map(k))
        return self


class RoutingRuleRedirect(TeaModel):
    def __init__(
        self,
        enable_replace_prefix: bool = None,
        host_name: str = None,
        http_redirect_code: int = None,
        mirror_check_md_5: bool = None,
        mirror_follow_redirect: bool = None,
        mirror_headers: RoutingRuleRedirectMirrorHeaders = None,
        mirror_pass_query_string: bool = None,
        mirror_url: str = None,
        pass_query_string: bool = None,
        protocol: str = None,
        redirect_type: str = None,
        replace_key_prefix_with: str = None,
        replace_key_with: str = None,
        transparent_mirror_response_codes: str = None,
    ):
        self.enable_replace_prefix = enable_replace_prefix
        self.host_name = host_name
        self.http_redirect_code = http_redirect_code
        self.mirror_check_md_5 = mirror_check_md_5
        self.mirror_follow_redirect = mirror_follow_redirect
        self.mirror_headers = mirror_headers
        self.mirror_pass_query_string = mirror_pass_query_string
        self.mirror_url = mirror_url
        self.pass_query_string = pass_query_string
        self.protocol = protocol
        self.redirect_type = redirect_type
        self.replace_key_prefix_with = replace_key_prefix_with
        self.replace_key_with = replace_key_with
        self.transparent_mirror_response_codes = transparent_mirror_response_codes

    def validate(self):
        if self.mirror_headers:
            self.mirror_headers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_replace_prefix is not None:
            result['EnableReplacePrefix'] = self.enable_replace_prefix
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.http_redirect_code is not None:
            result['HttpRedirectCode'] = self.http_redirect_code
        if self.mirror_check_md_5 is not None:
            result['MirrorCheckMd5'] = self.mirror_check_md_5
        if self.mirror_follow_redirect is not None:
            result['MirrorFollowRedirect'] = self.mirror_follow_redirect
        if self.mirror_headers is not None:
            result['MirrorHeaders'] = self.mirror_headers.to_map()
        if self.mirror_pass_query_string is not None:
            result['MirrorPassQueryString'] = self.mirror_pass_query_string
        if self.mirror_url is not None:
            result['MirrorURL'] = self.mirror_url
        if self.pass_query_string is not None:
            result['PassQueryString'] = self.pass_query_string
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.redirect_type is not None:
            result['RedirectType'] = self.redirect_type
        if self.replace_key_prefix_with is not None:
            result['ReplaceKeyPrefixWith'] = self.replace_key_prefix_with
        if self.replace_key_with is not None:
            result['ReplaceKeyWith'] = self.replace_key_with
        if self.transparent_mirror_response_codes is not None:
            result['TransparentMirrorResponseCodes'] = self.transparent_mirror_response_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableReplacePrefix') is not None:
            self.enable_replace_prefix = m.get('EnableReplacePrefix')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HttpRedirectCode') is not None:
            self.http_redirect_code = m.get('HttpRedirectCode')
        if m.get('MirrorCheckMd5') is not None:
            self.mirror_check_md_5 = m.get('MirrorCheckMd5')
        if m.get('MirrorFollowRedirect') is not None:
            self.mirror_follow_redirect = m.get('MirrorFollowRedirect')
        if m.get('MirrorHeaders') is not None:
            temp_model = RoutingRuleRedirectMirrorHeaders()
            self.mirror_headers = temp_model.from_map(m['MirrorHeaders'])
        if m.get('MirrorPassQueryString') is not None:
            self.mirror_pass_query_string = m.get('MirrorPassQueryString')
        if m.get('MirrorURL') is not None:
            self.mirror_url = m.get('MirrorURL')
        if m.get('PassQueryString') is not None:
            self.pass_query_string = m.get('PassQueryString')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RedirectType') is not None:
            self.redirect_type = m.get('RedirectType')
        if m.get('ReplaceKeyPrefixWith') is not None:
            self.replace_key_prefix_with = m.get('ReplaceKeyPrefixWith')
        if m.get('ReplaceKeyWith') is not None:
            self.replace_key_with = m.get('ReplaceKeyWith')
        if m.get('TransparentMirrorResponseCodes') is not None:
            self.transparent_mirror_response_codes = m.get('TransparentMirrorResponseCodes')
        return self


class RoutingRule(TeaModel):
    def __init__(
        self,
        condition: RoutingRuleCondition = None,
        redirect: RoutingRuleRedirect = None,
        rule_number: int = None,
    ):
        self.condition = condition
        self.redirect = redirect
        self.rule_number = rule_number

    def validate(self):
        if self.condition:
            self.condition.validate()
        if self.redirect:
            self.redirect.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition.to_map()
        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()
        if self.rule_number is not None:
            result['RuleNumber'] = self.rule_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            temp_model = RoutingRuleCondition()
            self.condition = temp_model.from_map(m['Condition'])
        if m.get('Redirect') is not None:
            temp_model = RoutingRuleRedirect()
            self.redirect = temp_model.from_map(m['Redirect'])
        if m.get('RuleNumber') is not None:
            self.rule_number = m.get('RuleNumber')
        return self


class SelectMetaRequest(TeaModel):
    def __init__(
        self,
        input_serialization: InputSerialization = None,
        overwrite_if_exists: bool = None,
    ):
        self.input_serialization = input_serialization
        self.overwrite_if_exists = overwrite_if_exists

    def validate(self):
        if self.input_serialization:
            self.input_serialization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_serialization is not None:
            result['InputSerialization'] = self.input_serialization.to_map()
        if self.overwrite_if_exists is not None:
            result['OverwriteIfExists'] = self.overwrite_if_exists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputSerialization') is not None:
            temp_model = InputSerialization()
            self.input_serialization = temp_model.from_map(m['InputSerialization'])
        if m.get('OverwriteIfExists') is not None:
            self.overwrite_if_exists = m.get('OverwriteIfExists')
        return self


class SelectMetaStatus(TeaModel):
    def __init__(
        self,
        cols_count: int = None,
        error_message: str = None,
        offset: int = None,
        rows_count: int = None,
        splits_count: int = None,
        status: int = None,
        total_scanned_bytes: int = None,
    ):
        self.cols_count = cols_count
        self.error_message = error_message
        self.offset = offset
        self.rows_count = rows_count
        self.splits_count = splits_count
        self.status = status
        self.total_scanned_bytes = total_scanned_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cols_count is not None:
            result['ColsCount'] = self.cols_count
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.rows_count is not None:
            result['RowsCount'] = self.rows_count
        if self.splits_count is not None:
            result['SplitsCount'] = self.splits_count
        if self.status is not None:
            result['Status'] = self.status
        if self.total_scanned_bytes is not None:
            result['TotalScannedBytes'] = self.total_scanned_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColsCount') is not None:
            self.cols_count = m.get('ColsCount')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RowsCount') is not None:
            self.rows_count = m.get('RowsCount')
        if m.get('SplitsCount') is not None:
            self.splits_count = m.get('SplitsCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalScannedBytes') is not None:
            self.total_scanned_bytes = m.get('TotalScannedBytes')
        return self


class SelectRequestOptions(TeaModel):
    def __init__(
        self,
        max_skipped_records_allowed: int = None,
        skip_partial_data_record: bool = None,
    ):
        self.max_skipped_records_allowed = max_skipped_records_allowed
        self.skip_partial_data_record = skip_partial_data_record

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_skipped_records_allowed is not None:
            result['MaxSkippedRecordsAllowed'] = self.max_skipped_records_allowed
        if self.skip_partial_data_record is not None:
            result['SkipPartialDataRecord'] = self.skip_partial_data_record
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSkippedRecordsAllowed') is not None:
            self.max_skipped_records_allowed = m.get('MaxSkippedRecordsAllowed')
        if m.get('SkipPartialDataRecord') is not None:
            self.skip_partial_data_record = m.get('SkipPartialDataRecord')
        return self


class SelectRequest(TeaModel):
    def __init__(
        self,
        expression: str = None,
        input_serialization: InputSerialization = None,
        options: SelectRequestOptions = None,
        output_serialization: OutputSerialization = None,
    ):
        self.expression = expression
        self.input_serialization = input_serialization
        self.options = options
        self.output_serialization = output_serialization

    def validate(self):
        if self.input_serialization:
            self.input_serialization.validate()
        if self.options:
            self.options.validate()
        if self.output_serialization:
            self.output_serialization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.input_serialization is not None:
            result['InputSerialization'] = self.input_serialization.to_map()
        if self.options is not None:
            result['Options'] = self.options.to_map()
        if self.output_serialization is not None:
            result['OutputSerialization'] = self.output_serialization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('InputSerialization') is not None:
            temp_model = InputSerialization()
            self.input_serialization = temp_model.from_map(m['InputSerialization'])
        if m.get('Options') is not None:
            temp_model = SelectRequestOptions()
            self.options = temp_model.from_map(m['Options'])
        if m.get('OutputSerialization') is not None:
            temp_model = OutputSerialization()
            self.output_serialization = temp_model.from_map(m['OutputSerialization'])
        return self


class ServerSideEncryptionRule(TeaModel):
    def __init__(
        self,
        apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault = None,
    ):
        self.apply_server_side_encryption_by_default = apply_server_side_encryption_by_default

    def validate(self):
        if self.apply_server_side_encryption_by_default:
            self.apply_server_side_encryption_by_default.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_server_side_encryption_by_default is not None:
            result['ApplyServerSideEncryptionByDefault'] = self.apply_server_side_encryption_by_default.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyServerSideEncryptionByDefault') is not None:
            temp_model = ApplyServerSideEncryptionByDefault()
            self.apply_server_side_encryption_by_default = temp_model.from_map(m['ApplyServerSideEncryptionByDefault'])
        return self


class Tag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagSet(TeaModel):
    def __init__(
        self,
        tags: List[Tag] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class Tagging(TeaModel):
    def __init__(
        self,
        tag_set: TagSet = None,
    ):
        self.tag_set = tag_set

    def validate(self):
        if self.tag_set:
            self.tag_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_set is not None:
            result['TagSet'] = self.tag_set.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagSet') is not None:
            temp_model = TagSet()
            self.tag_set = temp_model.from_map(m['TagSet'])
        return self


class TransferAccelerationConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class Upload(TeaModel):
    def __init__(
        self,
        initiated: str = None,
        key: str = None,
        upload_id: str = None,
    ):
        self.initiated = initiated
        self.key = key
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initiated is not None:
            result['Initiated'] = self.initiated
        if self.key is not None:
            result['Key'] = self.key
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Initiated') is not None:
            self.initiated = m.get('Initiated')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        return self


class VersioningConfiguration(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class WebsiteConfigurationRoutingRules(TeaModel):
    def __init__(
        self,
        routing_rule: List[RoutingRule] = None,
    ):
        self.routing_rule = routing_rule

    def validate(self):
        if self.routing_rule:
            for k in self.routing_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoutingRule'] = []
        if self.routing_rule is not None:
            for k in self.routing_rule:
                result['RoutingRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.routing_rule = []
        if m.get('RoutingRule') is not None:
            for k in m.get('RoutingRule'):
                temp_model = RoutingRule()
                self.routing_rule.append(temp_model.from_map(k))
        return self


class WebsiteConfiguration(TeaModel):
    def __init__(
        self,
        error_document: ErrorDocument = None,
        index_document: IndexDocument = None,
        routing_rules: WebsiteConfigurationRoutingRules = None,
    ):
        self.error_document = error_document
        self.index_document = index_document
        self.routing_rules = routing_rules

    def validate(self):
        if self.error_document:
            self.error_document.validate()
        if self.index_document:
            self.index_document.validate()
        if self.routing_rules:
            self.routing_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_document is not None:
            result['ErrorDocument'] = self.error_document.to_map()
        if self.index_document is not None:
            result['IndexDocument'] = self.index_document.to_map()
        if self.routing_rules is not None:
            result['RoutingRules'] = self.routing_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDocument') is not None:
            temp_model = ErrorDocument()
            self.error_document = temp_model.from_map(m['ErrorDocument'])
        if m.get('IndexDocument') is not None:
            temp_model = IndexDocument()
            self.index_document = temp_model.from_map(m['IndexDocument'])
        if m.get('RoutingRules') is not None:
            temp_model = WebsiteConfigurationRoutingRules()
            self.routing_rules = temp_model.from_map(m['RoutingRules'])
        return self


class AbortBucketWormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class AbortMultipartUploadRequest(TeaModel):
    def __init__(
        self,
        upload_id: str = None,
    ):
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.upload_id is not None:
            result['uploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uploadId') is not None:
            self.upload_id = m.get('uploadId')
        return self


class AbortMultipartUploadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class AppendObjectHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        cache_control: str = None,
        content_disposition: str = None,
        content_encoding: str = None,
        content_md5: str = None,
        expires: str = None,
        meta_data: Dict[str, str] = None,
        acl: str = None,
        server_side_encryption: str = None,
        storage_class: str = None,
    ):
        self.common_headers = common_headers
        self.cache_control = cache_control
        self.content_disposition = content_disposition
        self.content_encoding = content_encoding
        self.content_md5 = content_md5
        self.expires = expires
        self.meta_data = meta_data
        self.acl = acl
        self.server_side_encryption = server_side_encryption
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.cache_control is not None:
            result['Cache-Control'] = self.cache_control
        if self.content_disposition is not None:
            result['Content-Disposition'] = self.content_disposition
        if self.content_encoding is not None:
            result['Content-Encoding'] = self.content_encoding
        if self.content_md5 is not None:
            result['Content-MD5'] = self.content_md5
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.meta_data is not None:
            result['x-oss-meta-*'] = self.meta_data
        if self.acl is not None:
            result['x-oss-object-acl'] = self.acl
        if self.server_side_encryption is not None:
            result['x-oss-server-side-encryption'] = self.server_side_encryption
        if self.storage_class is not None:
            result['x-oss-storage-class'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Cache-Control') is not None:
            self.cache_control = m.get('Cache-Control')
        if m.get('Content-Disposition') is not None:
            self.content_disposition = m.get('Content-Disposition')
        if m.get('Content-Encoding') is not None:
            self.content_encoding = m.get('Content-Encoding')
        if m.get('Content-MD5') is not None:
            self.content_md5 = m.get('Content-MD5')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('x-oss-meta-*') is not None:
            self.meta_data = m.get('x-oss-meta-*')
        if m.get('x-oss-object-acl') is not None:
            self.acl = m.get('x-oss-object-acl')
        if m.get('x-oss-server-side-encryption') is not None:
            self.server_side_encryption = m.get('x-oss-server-side-encryption')
        if m.get('x-oss-storage-class') is not None:
            self.storage_class = m.get('x-oss-storage-class')
        return self


class AppendObjectRequest(TeaModel):
    def __init__(
        self,
        body: BinaryIO = None,
        position: int = None,
    ):
        self.body = body
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.position is not None:
            result['position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('position') is not None:
            self.position = m.get('position')
        return self


class AppendObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CompleteBucketWormRequest(TeaModel):
    def __init__(
        self,
        worm_id: str = None,
    ):
        self.worm_id = worm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.worm_id is not None:
            result['wormId'] = self.worm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('wormId') is not None:
            self.worm_id = m.get('wormId')
        return self


class CompleteBucketWormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CompleteMultipartUploadHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        complete_all: str = None,
        forbid_overwrite: str = None,
    ):
        self.common_headers = common_headers
        self.complete_all = complete_all
        self.forbid_overwrite = forbid_overwrite

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.complete_all is not None:
            result['x-oss-complete-all'] = self.complete_all
        if self.forbid_overwrite is not None:
            result['x-oss-forbid-overwrite'] = self.forbid_overwrite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-oss-complete-all') is not None:
            self.complete_all = m.get('x-oss-complete-all')
        if m.get('x-oss-forbid-overwrite') is not None:
            self.forbid_overwrite = m.get('x-oss-forbid-overwrite')
        return self


class CompleteMultipartUploadRequest(TeaModel):
    def __init__(
        self,
        complete_multipart_upload: CompleteMultipartUpload = None,
        encoding_type: str = None,
        upload_id: str = None,
    ):
        self.complete_multipart_upload = complete_multipart_upload
        self.encoding_type = encoding_type
        self.upload_id = upload_id

    def validate(self):
        if self.complete_multipart_upload:
            self.complete_multipart_upload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_multipart_upload is not None:
            result['completeMultipartUpload'] = self.complete_multipart_upload.to_map()
        if self.encoding_type is not None:
            result['encoding-type'] = self.encoding_type
        if self.upload_id is not None:
            result['uploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completeMultipartUpload') is not None:
            temp_model = CompleteMultipartUpload()
            self.complete_multipart_upload = temp_model.from_map(m['completeMultipartUpload'])
        if m.get('encoding-type') is not None:
            self.encoding_type = m.get('encoding-type')
        if m.get('uploadId') is not None:
            self.upload_id = m.get('uploadId')
        return self


class CompleteMultipartUploadResponseBody(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        etag: str = None,
        encoding_type: str = None,
        key: str = None,
        location: str = None,
    ):
        self.bucket = bucket
        self.etag = etag
        self.encoding_type = encoding_type
        self.key = key
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.key is not None:
            result['Key'] = self.key
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class CompleteMultipartUploadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompleteMultipartUploadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CompleteMultipartUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyObjectHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        copy_source: str = None,
        copy_source_if_match: str = None,
        copy_source_if_modified_since: str = None,
        copy_source_if_none_match: str = None,
        copy_source_if_unmodified_since: str = None,
        forbid_overwrite: str = None,
        meta_data: Dict[str, str] = None,
        metadata_directive: str = None,
        acl: str = None,
        server_side_encryption: str = None,
        sse_key_id: str = None,
        storage_class: str = None,
        tagging: str = None,
        tagging_directive: str = None,
    ):
        self.common_headers = common_headers
        self.copy_source = copy_source
        self.copy_source_if_match = copy_source_if_match
        self.copy_source_if_modified_since = copy_source_if_modified_since
        self.copy_source_if_none_match = copy_source_if_none_match
        self.copy_source_if_unmodified_since = copy_source_if_unmodified_since
        self.forbid_overwrite = forbid_overwrite
        self.meta_data = meta_data
        self.metadata_directive = metadata_directive
        self.acl = acl
        self.server_side_encryption = server_side_encryption
        self.sse_key_id = sse_key_id
        self.storage_class = storage_class
        self.tagging = tagging
        self.tagging_directive = tagging_directive

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.copy_source is not None:
            result['x-oss-copy-source'] = self.copy_source
        if self.copy_source_if_match is not None:
            result['x-oss-copy-source-if-match'] = self.copy_source_if_match
        if self.copy_source_if_modified_since is not None:
            result['x-oss-copy-source-if-modified-since'] = self.copy_source_if_modified_since
        if self.copy_source_if_none_match is not None:
            result['x-oss-copy-source-if-none-match'] = self.copy_source_if_none_match
        if self.copy_source_if_unmodified_since is not None:
            result['x-oss-copy-source-if-unmodified-since'] = self.copy_source_if_unmodified_since
        if self.forbid_overwrite is not None:
            result['x-oss-forbid-overwrite'] = self.forbid_overwrite
        if self.meta_data is not None:
            result['x-oss-meta-*'] = self.meta_data
        if self.metadata_directive is not None:
            result['x-oss-metadata-directive'] = self.metadata_directive
        if self.acl is not None:
            result['x-oss-object-acl'] = self.acl
        if self.server_side_encryption is not None:
            result['x-oss-server-side-encryption'] = self.server_side_encryption
        if self.sse_key_id is not None:
            result['x-oss-server-side-encryption-key-id'] = self.sse_key_id
        if self.storage_class is not None:
            result['x-oss-storage-class'] = self.storage_class
        if self.tagging is not None:
            result['x-oss-tagging'] = self.tagging
        if self.tagging_directive is not None:
            result['x-oss-tagging-directive'] = self.tagging_directive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-oss-copy-source') is not None:
            self.copy_source = m.get('x-oss-copy-source')
        if m.get('x-oss-copy-source-if-match') is not None:
            self.copy_source_if_match = m.get('x-oss-copy-source-if-match')
        if m.get('x-oss-copy-source-if-modified-since') is not None:
            self.copy_source_if_modified_since = m.get('x-oss-copy-source-if-modified-since')
        if m.get('x-oss-copy-source-if-none-match') is not None:
            self.copy_source_if_none_match = m.get('x-oss-copy-source-if-none-match')
        if m.get('x-oss-copy-source-if-unmodified-since') is not None:
            self.copy_source_if_unmodified_since = m.get('x-oss-copy-source-if-unmodified-since')
        if m.get('x-oss-forbid-overwrite') is not None:
            self.forbid_overwrite = m.get('x-oss-forbid-overwrite')
        if m.get('x-oss-meta-*') is not None:
            self.meta_data = m.get('x-oss-meta-*')
        if m.get('x-oss-metadata-directive') is not None:
            self.metadata_directive = m.get('x-oss-metadata-directive')
        if m.get('x-oss-object-acl') is not None:
            self.acl = m.get('x-oss-object-acl')
        if m.get('x-oss-server-side-encryption') is not None:
            self.server_side_encryption = m.get('x-oss-server-side-encryption')
        if m.get('x-oss-server-side-encryption-key-id') is not None:
            self.sse_key_id = m.get('x-oss-server-side-encryption-key-id')
        if m.get('x-oss-storage-class') is not None:
            self.storage_class = m.get('x-oss-storage-class')
        if m.get('x-oss-tagging') is not None:
            self.tagging = m.get('x-oss-tagging')
        if m.get('x-oss-tagging-directive') is not None:
            self.tagging_directive = m.get('x-oss-tagging-directive')
        return self


class CopyObjectResponseBody(TeaModel):
    def __init__(
        self,
        etag: str = None,
        last_modified: str = None,
    ):
        self.etag = etag
        self.last_modified = last_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class CopyObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyObjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CopyObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSelectObjectMetaRequest(TeaModel):
    def __init__(
        self,
        select_meta_request: SelectMetaRequest = None,
    ):
        self.select_meta_request = select_meta_request

    def validate(self):
        if self.select_meta_request:
            self.select_meta_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select_meta_request is not None:
            result['body'] = self.select_meta_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SelectMetaRequest()
            self.select_meta_request = temp_model.from_map(m['body'])
        return self


class CreateSelectObjectMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SelectMetaStatus = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SelectMetaStatus()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketCorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketEncryptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketInventoryRequest(TeaModel):
    def __init__(
        self,
        inventory_id: str = None,
    ):
        self.inventory_id = inventory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory_id is not None:
            result['inventoryId'] = self.inventory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inventoryId') is not None:
            self.inventory_id = m.get('inventoryId')
        return self


class DeleteBucketInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketLifecycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketReplicationRequest(TeaModel):
    def __init__(
        self,
        body: ReplicationRules = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['ReplicationRules'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReplicationRules') is not None:
            temp_model = ReplicationRules()
            self.body = temp_model.from_map(m['ReplicationRules'])
        return self


class DeleteBucketReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteBucketWebsiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteLiveChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteMultipleObjectsRequest(TeaModel):
    def __init__(
        self,
        delete: Delete = None,
        encoding_type: str = None,
    ):
        self.delete = delete
        self.encoding_type = encoding_type

    def validate(self):
        if self.delete:
            self.delete.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete is not None:
            result['Delete'] = self.delete.to_map()
        if self.encoding_type is not None:
            result['encoding-type'] = self.encoding_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delete') is not None:
            temp_model = Delete()
            self.delete = temp_model.from_map(m['Delete'])
        if m.get('encoding-type') is not None:
            self.encoding_type = m.get('encoding-type')
        return self


class DeleteMultipleObjectsResponseBody(TeaModel):
    def __init__(
        self,
        deleted: List[DeletedObject] = None,
        encoding_type: str = None,
    ):
        self.deleted = deleted
        self.encoding_type = encoding_type

    def validate(self):
        if self.deleted:
            for k in self.deleted:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Deleted'] = []
        if self.deleted is not None:
            for k in self.deleted:
                result['Deleted'].append(k.to_map() if k else None)
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deleted = []
        if m.get('Deleted') is not None:
            for k in m.get('Deleted'):
                temp_model = DeletedObject()
                self.deleted.append(temp_model.from_map(k))
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        return self


class DeleteMultipleObjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMultipleObjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteMultipleObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteObjectRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class DeleteObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteObjectTaggingRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class DeleteObjectTaggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        regions: str = None,
    ):
        self.regions = regions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['regions'] = self.regions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        region_infos: List[RegionInfo] = None,
    ):
        self.region_infos = region_infos

    def validate(self):
        if self.region_infos:
            for k in self.region_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionInfo'] = []
        if self.region_infos is not None:
            for k in self.region_infos:
                result['RegionInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_infos = []
        if m.get('RegionInfo') is not None:
            for k in m.get('RegionInfo'):
                temp_model = RegionInfo()
                self.region_infos.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtendBucketWormRequest(TeaModel):
    def __init__(
        self,
        extend_worm_configuration: ExtendWormConfiguration = None,
        worm_id: str = None,
    ):
        self.extend_worm_configuration = extend_worm_configuration
        self.worm_id = worm_id

    def validate(self):
        if self.extend_worm_configuration:
            self.extend_worm_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_worm_configuration is not None:
            result['extendWormConfiguration'] = self.extend_worm_configuration.to_map()
        if self.worm_id is not None:
            result['wormId'] = self.worm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendWormConfiguration') is not None:
            temp_model = ExtendWormConfiguration()
            self.extend_worm_configuration = temp_model.from_map(m['extendWormConfiguration'])
        if m.get('wormId') is not None:
            self.worm_id = m.get('wormId')
        return self


class ExtendBucketWormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetBucketAclResponseBodyAccessControlList(TeaModel):
    def __init__(
        self,
        grant: str = None,
    ):
        self.grant = grant

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant is not None:
            result['Grant'] = self.grant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grant') is not None:
            self.grant = m.get('Grant')
        return self


class GetBucketAclResponseBody(TeaModel):
    def __init__(
        self,
        access_control_list: GetBucketAclResponseBodyAccessControlList = None,
        owner: Owner = None,
    ):
        self.access_control_list = access_control_list
        self.owner = owner

    def validate(self):
        if self.access_control_list:
            self.access_control_list.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list is not None:
            result['AccessControlList'] = self.access_control_list.to_map()
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlList') is not None:
            temp_model = GetBucketAclResponseBodyAccessControlList()
            self.access_control_list = temp_model.from_map(m['AccessControlList'])
        if m.get('Owner') is not None:
            temp_model = Owner()
            self.owner = temp_model.from_map(m['Owner'])
        return self


class GetBucketAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketCorsResponseBody(TeaModel):
    def __init__(
        self,
        corsrule: List[CORSRule] = None,
        response_vary: bool = None,
    ):
        self.corsrule = corsrule
        self.response_vary = response_vary

    def validate(self):
        if self.corsrule:
            for k in self.corsrule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CORSRule'] = []
        if self.corsrule is not None:
            for k in self.corsrule:
                result['CORSRule'].append(k.to_map() if k else None)
        if self.response_vary is not None:
            result['ResponseVary'] = self.response_vary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.corsrule = []
        if m.get('CORSRule') is not None:
            for k in m.get('CORSRule'):
                temp_model = CORSRule()
                self.corsrule.append(temp_model.from_map(k))
        if m.get('ResponseVary') is not None:
            self.response_vary = m.get('ResponseVary')
        return self


class GetBucketCorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketCorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketCorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketEncryptionResponseBody(TeaModel):
    def __init__(
        self,
        apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault = None,
    ):
        self.apply_server_side_encryption_by_default = apply_server_side_encryption_by_default

    def validate(self):
        if self.apply_server_side_encryption_by_default:
            self.apply_server_side_encryption_by_default.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_server_side_encryption_by_default is not None:
            result['ApplyServerSideEncryptionByDefault'] = self.apply_server_side_encryption_by_default.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyServerSideEncryptionByDefault') is not None:
            temp_model = ApplyServerSideEncryptionByDefault()
            self.apply_server_side_encryption_by_default = temp_model.from_map(m['ApplyServerSideEncryptionByDefault'])
        return self


class GetBucketEncryptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketEncryptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketEncryptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketInfoResponseBodyBucketInfoAccessControlList(TeaModel):
    def __init__(
        self,
        grant: str = None,
    ):
        self.grant = grant

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant is not None:
            result['Grant'] = self.grant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grant') is not None:
            self.grant = m.get('Grant')
        return self


class GetBucketInfoResponseBodyBucketInfo(TeaModel):
    def __init__(
        self,
        access_control_list: GetBucketInfoResponseBodyBucketInfoAccessControlList = None,
        comment: str = None,
        creation_date: str = None,
        cross_region_replication: str = None,
        extranet_endpoint: str = None,
        intranet_endpoint: str = None,
        location: str = None,
        name: str = None,
        owner: Owner = None,
        storage_class: str = None,
        transfer_acceleration: str = None,
    ):
        self.access_control_list = access_control_list
        self.comment = comment
        self.creation_date = creation_date
        self.cross_region_replication = cross_region_replication
        self.extranet_endpoint = extranet_endpoint
        self.intranet_endpoint = intranet_endpoint
        self.location = location
        self.name = name
        self.owner = owner
        self.storage_class = storage_class
        self.transfer_acceleration = transfer_acceleration

    def validate(self):
        if self.access_control_list:
            self.access_control_list.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list is not None:
            result['AccessControlList'] = self.access_control_list.to_map()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.cross_region_replication is not None:
            result['CrossRegionReplication'] = self.cross_region_replication
        if self.extranet_endpoint is not None:
            result['ExtranetEndpoint'] = self.extranet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.transfer_acceleration is not None:
            result['TransferAcceleration'] = self.transfer_acceleration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlList') is not None:
            temp_model = GetBucketInfoResponseBodyBucketInfoAccessControlList()
            self.access_control_list = temp_model.from_map(m['AccessControlList'])
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('CrossRegionReplication') is not None:
            self.cross_region_replication = m.get('CrossRegionReplication')
        if m.get('ExtranetEndpoint') is not None:
            self.extranet_endpoint = m.get('ExtranetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            temp_model = Owner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('TransferAcceleration') is not None:
            self.transfer_acceleration = m.get('TransferAcceleration')
        return self


class GetBucketInfoResponseBody(TeaModel):
    def __init__(
        self,
        bucket_info: GetBucketInfoResponseBodyBucketInfo = None,
    ):
        self.bucket_info = bucket_info

    def validate(self):
        if self.bucket_info:
            self.bucket_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_info is not None:
            result['Bucket'] = self.bucket_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            temp_model = GetBucketInfoResponseBodyBucketInfo()
            self.bucket_info = temp_model.from_map(m['Bucket'])
        return self


class GetBucketInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketInventoryRequest(TeaModel):
    def __init__(
        self,
        inventory_id: str = None,
    ):
        self.inventory_id = inventory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory_id is not None:
            result['inventoryId'] = self.inventory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inventoryId') is not None:
            self.inventory_id = m.get('inventoryId')
        return self


class GetBucketInventoryResponseBodyOptionalFields(TeaModel):
    def __init__(
        self,
        field: List[str] = None,
    ):
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        return self


class GetBucketInventoryResponseBody(TeaModel):
    def __init__(
        self,
        destination: InventoryDestination = None,
        filter: InventoryFilter = None,
        id: str = None,
        included_object_versions: str = None,
        is_enabled: bool = None,
        optional_fields: GetBucketInventoryResponseBodyOptionalFields = None,
        schedule: InventorySchedule = None,
    ):
        self.destination = destination
        self.filter = filter
        self.id = id
        self.included_object_versions = included_object_versions
        self.is_enabled = is_enabled
        self.optional_fields = optional_fields
        self.schedule = schedule

    def validate(self):
        if self.destination:
            self.destination.validate()
        if self.filter:
            self.filter.validate()
        if self.optional_fields:
            self.optional_fields.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.included_object_versions is not None:
            result['IncludedObjectVersions'] = self.included_object_versions
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.optional_fields is not None:
            result['OptionalFields'] = self.optional_fields.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            temp_model = InventoryDestination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('Filter') is not None:
            temp_model = InventoryFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludedObjectVersions') is not None:
            self.included_object_versions = m.get('IncludedObjectVersions')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('OptionalFields') is not None:
            temp_model = GetBucketInventoryResponseBodyOptionalFields()
            self.optional_fields = temp_model.from_map(m['OptionalFields'])
        if m.get('Schedule') is not None:
            temp_model = InventorySchedule()
            self.schedule = temp_model.from_map(m['Schedule'])
        return self


class GetBucketInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketInventoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketLifecycleResponseBody(TeaModel):
    def __init__(
        self,
        rules: List[LifecycleRule] = None,
    ):
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = LifecycleRule()
                self.rules.append(temp_model.from_map(k))
        return self


class GetBucketLifecycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketLifecycleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketLifecycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketLocationResponseBody(TeaModel):
    def __init__(
        self,
        location_constraint: str = None,
    ):
        self.location_constraint = location_constraint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_constraint is not None:
            result['LocationConstraint'] = self.location_constraint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationConstraint') is not None:
            self.location_constraint = m.get('LocationConstraint')
        return self


class GetBucketLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketLocationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketLoggingResponseBody(TeaModel):
    def __init__(
        self,
        logging_enabled: LoggingEnabled = None,
    ):
        self.logging_enabled = logging_enabled

    def validate(self):
        if self.logging_enabled:
            self.logging_enabled.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoggingEnabled') is not None:
            temp_model = LoggingEnabled()
            self.logging_enabled = temp_model.from_map(m['LoggingEnabled'])
        return self


class GetBucketLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketLoggingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: str = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetBucketRefererResponseBodyRefererList(TeaModel):
    def __init__(
        self,
        referer: List[str] = None,
    ):
        self.referer = referer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.referer is not None:
            result['Referer'] = self.referer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        return self


class GetBucketRefererResponseBody(TeaModel):
    def __init__(
        self,
        allow_empty_referer: bool = None,
        referer_list: GetBucketRefererResponseBodyRefererList = None,
    ):
        self.allow_empty_referer = allow_empty_referer
        self.referer_list = referer_list

    def validate(self):
        if self.referer_list:
            self.referer_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_empty_referer is not None:
            result['AllowEmptyReferer'] = self.allow_empty_referer
        if self.referer_list is not None:
            result['RefererList'] = self.referer_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowEmptyReferer') is not None:
            self.allow_empty_referer = m.get('AllowEmptyReferer')
        if m.get('RefererList') is not None:
            temp_model = GetBucketRefererResponseBodyRefererList()
            self.referer_list = temp_model.from_map(m['RefererList'])
        return self


class GetBucketRefererResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketRefererResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketRefererResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketReplicationResponseBody(TeaModel):
    def __init__(
        self,
        rules: List[ReplicationRule] = None,
    ):
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = ReplicationRule()
                self.rules.append(temp_model.from_map(k))
        return self


class GetBucketReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketReplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketReplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketReplicationLocationResponseBodyLocationTransferTypeConstraint(TeaModel):
    def __init__(
        self,
        location_transfer_types: List[LocationTransferType] = None,
    ):
        self.location_transfer_types = location_transfer_types

    def validate(self):
        if self.location_transfer_types:
            for k in self.location_transfer_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LocationTransferType'] = []
        if self.location_transfer_types is not None:
            for k in self.location_transfer_types:
                result['LocationTransferType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.location_transfer_types = []
        if m.get('LocationTransferType') is not None:
            for k in m.get('LocationTransferType'):
                temp_model = LocationTransferType()
                self.location_transfer_types.append(temp_model.from_map(k))
        return self


class GetBucketReplicationLocationResponseBody(TeaModel):
    def __init__(
        self,
        locations: List[str] = None,
        location_transfer_type_constraint: GetBucketReplicationLocationResponseBodyLocationTransferTypeConstraint = None,
    ):
        self.locations = locations
        self.location_transfer_type_constraint = location_transfer_type_constraint

    def validate(self):
        if self.location_transfer_type_constraint:
            self.location_transfer_type_constraint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locations is not None:
            result['Location'] = self.locations
        if self.location_transfer_type_constraint is not None:
            result['LocationTransferTypeConstraint'] = self.location_transfer_type_constraint.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.locations = m.get('Location')
        if m.get('LocationTransferTypeConstraint') is not None:
            temp_model = GetBucketReplicationLocationResponseBodyLocationTransferTypeConstraint()
            self.location_transfer_type_constraint = temp_model.from_map(m['LocationTransferTypeConstraint'])
        return self


class GetBucketReplicationLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketReplicationLocationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketReplicationLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketReplicationProgressRequest(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['rule-id'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rule-id') is not None:
            self.rule_id = m.get('rule-id')
        return self


class GetBucketReplicationProgressResponseBody(TeaModel):
    def __init__(
        self,
        rule: ReplicationProgressRule = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule is not None:
            result['Rule'] = self.rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            temp_model = ReplicationProgressRule()
            self.rule = temp_model.from_map(m['Rule'])
        return self


class GetBucketReplicationProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketReplicationProgressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketReplicationProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketRequestPaymentResponseBody(TeaModel):
    def __init__(
        self,
        payer: str = None,
    ):
        self.payer = payer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payer is not None:
            result['Payer'] = self.payer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        return self


class GetBucketRequestPaymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketRequestPaymentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketRequestPaymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketTagsResponseBody(TeaModel):
    def __init__(
        self,
        tag_set: TagSet = None,
    ):
        self.tag_set = tag_set

    def validate(self):
        if self.tag_set:
            self.tag_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_set is not None:
            result['TagSet'] = self.tag_set.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagSet') is not None:
            temp_model = TagSet()
            self.tag_set = temp_model.from_map(m['TagSet'])
        return self


class GetBucketTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketTransferAccelerationResponseBody(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class GetBucketTransferAccelerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketTransferAccelerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketTransferAccelerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketVersioningResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetBucketVersioningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketVersioningResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketVersioningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketWebsiteResponseBodyRoutingRules(TeaModel):
    def __init__(
        self,
        routing_rules: List[RoutingRule] = None,
    ):
        self.routing_rules = routing_rules

    def validate(self):
        if self.routing_rules:
            for k in self.routing_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoutingRule'] = []
        if self.routing_rules is not None:
            for k in self.routing_rules:
                result['RoutingRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.routing_rules = []
        if m.get('RoutingRule') is not None:
            for k in m.get('RoutingRule'):
                temp_model = RoutingRule()
                self.routing_rules.append(temp_model.from_map(k))
        return self


class GetBucketWebsiteResponseBody(TeaModel):
    def __init__(
        self,
        error_document: ErrorDocument = None,
        index_document: IndexDocument = None,
        routing_rules: GetBucketWebsiteResponseBodyRoutingRules = None,
    ):
        self.error_document = error_document
        self.index_document = index_document
        self.routing_rules = routing_rules

    def validate(self):
        if self.error_document:
            self.error_document.validate()
        if self.index_document:
            self.index_document.validate()
        if self.routing_rules:
            self.routing_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_document is not None:
            result['ErrorDocument'] = self.error_document.to_map()
        if self.index_document is not None:
            result['IndexDocument'] = self.index_document.to_map()
        if self.routing_rules is not None:
            result['RoutingRules'] = self.routing_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDocument') is not None:
            temp_model = ErrorDocument()
            self.error_document = temp_model.from_map(m['ErrorDocument'])
        if m.get('IndexDocument') is not None:
            temp_model = IndexDocument()
            self.index_document = temp_model.from_map(m['IndexDocument'])
        if m.get('RoutingRules') is not None:
            temp_model = GetBucketWebsiteResponseBodyRoutingRules()
            self.routing_rules = temp_model.from_map(m['RoutingRules'])
        return self


class GetBucketWebsiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketWebsiteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketWebsiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketWormResponseBody(TeaModel):
    def __init__(
        self,
        creation_date: str = None,
        retention_period_in_days: int = None,
        state: str = None,
        worm_id: str = None,
    ):
        self.creation_date = creation_date
        self.retention_period_in_days = retention_period_in_days
        self.state = state
        self.worm_id = worm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.retention_period_in_days is not None:
            result['RetentionPeriodInDays'] = self.retention_period_in_days
        if self.state is not None:
            result['State'] = self.state
        if self.worm_id is not None:
            result['WormId'] = self.worm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('RetentionPeriodInDays') is not None:
            self.retention_period_in_days = m.get('RetentionPeriodInDays')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('WormId') is not None:
            self.worm_id = m.get('WormId')
        return self


class GetBucketWormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketWormResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBucketWormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveChannelHistoryResponseBody(TeaModel):
    def __init__(
        self,
        live_records: List[LiveRecord] = None,
    ):
        self.live_records = live_records

    def validate(self):
        if self.live_records:
            for k in self.live_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveRecord'] = []
        if self.live_records is not None:
            for k in self.live_records:
                result['LiveRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_records = []
        if m.get('LiveRecord') is not None:
            for k in m.get('LiveRecord'):
                temp_model = LiveRecord()
                self.live_records.append(temp_model.from_map(k))
        return self


class GetLiveChannelHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLiveChannelHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLiveChannelHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveChannelInfoResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        status: str = None,
        target: LiveChannelTarget = None,
    ):
        self.description = description
        self.status = status
        self.target = target

    def validate(self):
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            temp_model = LiveChannelTarget()
            self.target = temp_model.from_map(m['Target'])
        return self


class GetLiveChannelInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLiveChannelInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLiveChannelInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveChannelStatResponseBody(TeaModel):
    def __init__(
        self,
        audio: LiveChannelAudio = None,
        connected_time: str = None,
        remote_addr: str = None,
        status: str = None,
        video: LiveChannelVideo = None,
    ):
        self.audio = audio
        self.connected_time = connected_time
        self.remote_addr = remote_addr
        self.status = status
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()
        if self.connected_time is not None:
            result['ConnectedTime'] = self.connected_time
        if self.remote_addr is not None:
            result['RemoteAddr'] = self.remote_addr
        if self.status is not None:
            result['Status'] = self.status
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = LiveChannelAudio()
            self.audio = temp_model.from_map(m['Audio'])
        if m.get('ConnectedTime') is not None:
            self.connected_time = m.get('ConnectedTime')
        if m.get('RemoteAddr') is not None:
            self.remote_addr = m.get('RemoteAddr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Video') is not None:
            temp_model = LiveChannelVideo()
            self.video = temp_model.from_map(m['Video'])
        return self


class GetLiveChannelStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLiveChannelStatResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLiveChannelStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetObjectHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        accept_encoding: str = None,
        if_match: str = None,
        if_modified_since: str = None,
        if_none_match: str = None,
        if_unmodified_since: str = None,
        range: str = None,
    ):
        self.common_headers = common_headers
        self.accept_encoding = accept_encoding
        self.if_match = if_match
        self.if_modified_since = if_modified_since
        self.if_none_match = if_none_match
        self.if_unmodified_since = if_unmodified_since
        self.range = range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.accept_encoding is not None:
            result['Accept-Encoding'] = self.accept_encoding
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.if_modified_since is not None:
            result['If-Modified-Since'] = self.if_modified_since
        if self.if_none_match is not None:
            result['If-None-Match'] = self.if_none_match
        if self.if_unmodified_since is not None:
            result['If-Unmodified-Since'] = self.if_unmodified_since
        if self.range is not None:
            result['Range'] = self.range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Accept-Encoding') is not None:
            self.accept_encoding = m.get('Accept-Encoding')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('If-Modified-Since') is not None:
            self.if_modified_since = m.get('If-Modified-Since')
        if m.get('If-None-Match') is not None:
            self.if_none_match = m.get('If-None-Match')
        if m.get('If-Unmodified-Since') is not None:
            self.if_unmodified_since = m.get('If-Unmodified-Since')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        return self


class GetObjectRequest(TeaModel):
    def __init__(
        self,
        response_cache_control: str = None,
        response_content_disposition: str = None,
        response_content_encoding: str = None,
        response_content_language: str = None,
        response_content_type: str = None,
        response_expires: str = None,
    ):
        self.response_cache_control = response_cache_control
        self.response_content_disposition = response_content_disposition
        self.response_content_encoding = response_content_encoding
        self.response_content_language = response_content_language
        self.response_content_type = response_content_type
        self.response_expires = response_expires

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_cache_control is not None:
            result['response-cache-control'] = self.response_cache_control
        if self.response_content_disposition is not None:
            result['response-content-disposition'] = self.response_content_disposition
        if self.response_content_encoding is not None:
            result['response-content-encoding'] = self.response_content_encoding
        if self.response_content_language is not None:
            result['response-content-language'] = self.response_content_language
        if self.response_content_type is not None:
            result['response-content-type'] = self.response_content_type
        if self.response_expires is not None:
            result['response-expires'] = self.response_expires
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('response-cache-control') is not None:
            self.response_cache_control = m.get('response-cache-control')
        if m.get('response-content-disposition') is not None:
            self.response_content_disposition = m.get('response-content-disposition')
        if m.get('response-content-encoding') is not None:
            self.response_content_encoding = m.get('response-content-encoding')
        if m.get('response-content-language') is not None:
            self.response_content_language = m.get('response-content-language')
        if m.get('response-content-type') is not None:
            self.response_content_type = m.get('response-content-type')
        if m.get('response-expires') is not None:
            self.response_expires = m.get('response-expires')
        return self


class GetObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BinaryIO = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetObjectAclRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetObjectAclResponseBodyAccessControlList(TeaModel):
    def __init__(
        self,
        acl: str = None,
    ):
        self.acl = acl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['Grant'] = self.acl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grant') is not None:
            self.acl = m.get('Grant')
        return self


class GetObjectAclResponseBody(TeaModel):
    def __init__(
        self,
        access_control_list: GetObjectAclResponseBodyAccessControlList = None,
        owner: Owner = None,
    ):
        self.access_control_list = access_control_list
        self.owner = owner

    def validate(self):
        if self.access_control_list:
            self.access_control_list.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list is not None:
            result['AccessControlList'] = self.access_control_list.to_map()
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlList') is not None:
            temp_model = GetObjectAclResponseBodyAccessControlList()
            self.access_control_list = temp_model.from_map(m['AccessControlList'])
        if m.get('Owner') is not None:
            temp_model = Owner()
            self.owner = temp_model.from_map(m['Owner'])
        return self


class GetObjectAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetObjectAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetObjectAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetObjectMetaRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetObjectMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetObjectTaggingRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetObjectTaggingResponseBody(TeaModel):
    def __init__(
        self,
        tag_set: TagSet = None,
    ):
        self.tag_set = tag_set

    def validate(self):
        if self.tag_set:
            self.tag_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_set is not None:
            result['TagSet'] = self.tag_set.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagSet') is not None:
            temp_model = TagSet()
            self.tag_set = temp_model.from_map(m['TagSet'])
        return self


class GetObjectTaggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetObjectTaggingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetObjectTaggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSymlinkRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetSymlinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetVodPlaylistRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class GetVodPlaylistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BinaryIO = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class HeadObjectHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        if_modified_since: str = None,
        if_none_match: str = None,
        if_unmodified_since: str = None,
    ):
        self.common_headers = common_headers
        self.if_match = if_match
        self.if_modified_since = if_modified_since
        self.if_none_match = if_none_match
        self.if_unmodified_since = if_unmodified_since

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.if_modified_since is not None:
            result['If-Modified-Since'] = self.if_modified_since
        if self.if_none_match is not None:
            result['If-None-Match'] = self.if_none_match
        if self.if_unmodified_since is not None:
            result['If-Unmodified-Since'] = self.if_unmodified_since
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('If-Modified-Since') is not None:
            self.if_modified_since = m.get('If-Modified-Since')
        if m.get('If-None-Match') is not None:
            self.if_none_match = m.get('If-None-Match')
        if m.get('If-Unmodified-Since') is not None:
            self.if_unmodified_since = m.get('If-Unmodified-Since')
        return self


class HeadObjectRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class HeadObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class InitiateBucketWormRequest(TeaModel):
    def __init__(
        self,
        initiate_worm_configuration: InitiateWormConfiguration = None,
    ):
        self.initiate_worm_configuration = initiate_worm_configuration

    def validate(self):
        if self.initiate_worm_configuration:
            self.initiate_worm_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initiate_worm_configuration is not None:
            result['InitiateWormConfiguration'] = self.initiate_worm_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitiateWormConfiguration') is not None:
            temp_model = InitiateWormConfiguration()
            self.initiate_worm_configuration = temp_model.from_map(m['InitiateWormConfiguration'])
        return self


class InitiateBucketWormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class InitiateMultipartUploadHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        cache_control: str = None,
        content_disposition: str = None,
        content_encoding: str = None,
        expires: str = None,
        forbid_overwrite: str = None,
        sse_data_encryption: str = None,
        server_side_encryption: str = None,
        sse_key_id: str = None,
        storage_class: str = None,
        tagging: str = None,
    ):
        self.common_headers = common_headers
        self.cache_control = cache_control
        self.content_disposition = content_disposition
        self.content_encoding = content_encoding
        self.expires = expires
        self.forbid_overwrite = forbid_overwrite
        self.sse_data_encryption = sse_data_encryption
        self.server_side_encryption = server_side_encryption
        self.sse_key_id = sse_key_id
        self.storage_class = storage_class
        self.tagging = tagging

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.cache_control is not None:
            result['Cache-Control'] = self.cache_control
        if self.content_disposition is not None:
            result['Content-Disposition'] = self.content_disposition
        if self.content_encoding is not None:
            result['Content-Encoding'] = self.content_encoding
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.forbid_overwrite is not None:
            result['x-oss-forbid-overwrite'] = self.forbid_overwrite
        if self.sse_data_encryption is not None:
            result['x-oss-server-side-data-encryption'] = self.sse_data_encryption
        if self.server_side_encryption is not None:
            result['x-oss-server-side-encryption'] = self.server_side_encryption
        if self.sse_key_id is not None:
            result['x-oss-server-side-encryption-key-id'] = self.sse_key_id
        if self.storage_class is not None:
            result['x-oss-storage-class'] = self.storage_class
        if self.tagging is not None:
            result['x-oss-tagging'] = self.tagging
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Cache-Control') is not None:
            self.cache_control = m.get('Cache-Control')
        if m.get('Content-Disposition') is not None:
            self.content_disposition = m.get('Content-Disposition')
        if m.get('Content-Encoding') is not None:
            self.content_encoding = m.get('Content-Encoding')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('x-oss-forbid-overwrite') is not None:
            self.forbid_overwrite = m.get('x-oss-forbid-overwrite')
        if m.get('x-oss-server-side-data-encryption') is not None:
            self.sse_data_encryption = m.get('x-oss-server-side-data-encryption')
        if m.get('x-oss-server-side-encryption') is not None:
            self.server_side_encryption = m.get('x-oss-server-side-encryption')
        if m.get('x-oss-server-side-encryption-key-id') is not None:
            self.sse_key_id = m.get('x-oss-server-side-encryption-key-id')
        if m.get('x-oss-storage-class') is not None:
            self.storage_class = m.get('x-oss-storage-class')
        if m.get('x-oss-tagging') is not None:
            self.tagging = m.get('x-oss-tagging')
        return self


class InitiateMultipartUploadRequest(TeaModel):
    def __init__(
        self,
        encoding_type: str = None,
    ):
        self.encoding_type = encoding_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encoding_type is not None:
            result['encoding-type'] = self.encoding_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encoding-type') is not None:
            self.encoding_type = m.get('encoding-type')
        return self


class InitiateMultipartUploadResponseBody(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        encoding_type: str = None,
        key: str = None,
        upload_id: str = None,
    ):
        self.bucket = bucket
        self.encoding_type = encoding_type
        self.key = key
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.key is not None:
            result['Key'] = self.key
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        return self


class InitiateMultipartUploadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitiateMultipartUploadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = InitiateMultipartUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBucketInventoryRequest(TeaModel):
    def __init__(
        self,
        continuation_token: str = None,
    ):
        self.continuation_token = continuation_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.continuation_token is not None:
            result['continuation-token'] = self.continuation_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('continuation-token') is not None:
            self.continuation_token = m.get('continuation-token')
        return self


class ListBucketInventoryResponseBody(TeaModel):
    def __init__(
        self,
        inventory_configurations: List[InventoryConfiguration] = None,
        is_truncated: bool = None,
        next_continuation_token: str = None,
    ):
        self.inventory_configurations = inventory_configurations
        self.is_truncated = is_truncated
        self.next_continuation_token = next_continuation_token

    def validate(self):
        if self.inventory_configurations:
            for k in self.inventory_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InventoryConfiguration'] = []
        if self.inventory_configurations is not None:
            for k in self.inventory_configurations:
                result['InventoryConfiguration'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.next_continuation_token is not None:
            result['NextContinuationToken'] = self.next_continuation_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inventory_configurations = []
        if m.get('InventoryConfiguration') is not None:
            for k in m.get('InventoryConfiguration'):
                temp_model = InventoryConfiguration()
                self.inventory_configurations.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('NextContinuationToken') is not None:
            self.next_continuation_token = m.get('NextContinuationToken')
        return self


class ListBucketInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBucketInventoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListBucketInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBucketsRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_keys: int = None,
        prefix: str = None,
    ):
        self.marker = marker
        self.max_keys = max_keys
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['max-keys'] = self.max_keys
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('max-keys') is not None:
            self.max_keys = m.get('max-keys')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListBucketsResponseBodyBuckets(TeaModel):
    def __init__(
        self,
        buckets: List[Bucket] = None,
    ):
        self.buckets = buckets

    def validate(self):
        if self.buckets:
            for k in self.buckets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bucket'] = []
        if self.buckets is not None:
            for k in self.buckets:
                result['Bucket'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buckets = []
        if m.get('Bucket') is not None:
            for k in m.get('Bucket'):
                temp_model = Bucket()
                self.buckets.append(temp_model.from_map(k))
        return self


class ListBucketsResponseBody(TeaModel):
    def __init__(
        self,
        buckets: ListBucketsResponseBodyBuckets = None,
        is_truncated: bool = None,
        marker: str = None,
        max_keys: int = None,
        next_marker: str = None,
        owner: Owner = None,
        prefix: str = None,
    ):
        self.buckets = buckets
        self.is_truncated = is_truncated
        self.marker = marker
        self.max_keys = max_keys
        self.next_marker = next_marker
        self.owner = owner
        self.prefix = prefix

    def validate(self):
        if self.buckets:
            self.buckets.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buckets is not None:
            result['Buckets'] = self.buckets.to_map()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Buckets') is not None:
            temp_model = ListBucketsResponseBodyBuckets()
            self.buckets = temp_model.from_map(m['Buckets'])
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Owner') is not None:
            temp_model = Owner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListBucketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBucketsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveChannelRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_keys: int = None,
        prefix: str = None,
    ):
        self.marker = marker
        self.max_keys = max_keys
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['max-keys'] = self.max_keys
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('max-keys') is not None:
            self.max_keys = m.get('max-keys')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListLiveChannelResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        live_channels: List[LiveChannel] = None,
        marker: str = None,
        max_keys: int = None,
        next_marker: str = None,
        prefix: str = None,
    ):
        self.is_truncated = is_truncated
        self.live_channels = live_channels
        self.marker = marker
        self.max_keys = max_keys
        self.next_marker = next_marker
        self.prefix = prefix

    def validate(self):
        if self.live_channels:
            for k in self.live_channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        result['LiveChannel'] = []
        if self.live_channels is not None:
            for k in self.live_channels:
                result['LiveChannel'].append(k.to_map() if k else None)
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        self.live_channels = []
        if m.get('LiveChannel') is not None:
            for k in m.get('LiveChannel'):
                temp_model = LiveChannel()
                self.live_channels.append(temp_model.from_map(k))
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListLiveChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLiveChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLiveChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultipartUploadsRequest(TeaModel):
    def __init__(
        self,
        delimiter: str = None,
        encoding_type: str = None,
        key_marker: str = None,
        max_uploads: int = None,
        prefix: str = None,
        upload_id_marker: str = None,
    ):
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.key_marker = key_marker
        self.max_uploads = max_uploads
        self.prefix = prefix
        self.upload_id_marker = upload_id_marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delimiter is not None:
            result['delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['encoding-type'] = self.encoding_type
        if self.key_marker is not None:
            result['key-marker'] = self.key_marker
        if self.max_uploads is not None:
            result['max-uploads'] = self.max_uploads
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.upload_id_marker is not None:
            result['upload-id-marker'] = self.upload_id_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delimiter') is not None:
            self.delimiter = m.get('delimiter')
        if m.get('encoding-type') is not None:
            self.encoding_type = m.get('encoding-type')
        if m.get('key-marker') is not None:
            self.key_marker = m.get('key-marker')
        if m.get('max-uploads') is not None:
            self.max_uploads = m.get('max-uploads')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('upload-id-marker') is not None:
            self.upload_id_marker = m.get('upload-id-marker')
        return self


class ListMultipartUploadsResponseBody(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        common_prefixes: List[CommonPrefix] = None,
        delimiter: str = None,
        encoding_type: str = None,
        is_truncated: bool = None,
        key_marker: str = None,
        max_uploads: int = None,
        next_key_marker: str = None,
        next_upload_id_marker: str = None,
        prefix: str = None,
        uploads: List[Upload] = None,
        upload_id_marker: str = None,
    ):
        self.bucket = bucket
        self.common_prefixes = common_prefixes
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.is_truncated = is_truncated
        self.key_marker = key_marker
        self.max_uploads = max_uploads
        self.next_key_marker = next_key_marker
        self.next_upload_id_marker = next_upload_id_marker
        self.prefix = prefix
        self.uploads = uploads
        self.upload_id_marker = upload_id_marker

    def validate(self):
        if self.common_prefixes:
            for k in self.common_prefixes:
                if k:
                    k.validate()
        if self.uploads:
            for k in self.uploads:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        result['CommonPrefixes'] = []
        if self.common_prefixes is not None:
            for k in self.common_prefixes:
                result['CommonPrefixes'].append(k.to_map() if k else None)
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.key_marker is not None:
            result['KeyMarker'] = self.key_marker
        if self.max_uploads is not None:
            result['MaxUploads'] = self.max_uploads
        if self.next_key_marker is not None:
            result['NextKeyMarker'] = self.next_key_marker
        if self.next_upload_id_marker is not None:
            result['NextUploadIdMarker'] = self.next_upload_id_marker
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        result['Upload'] = []
        if self.uploads is not None:
            for k in self.uploads:
                result['Upload'].append(k.to_map() if k else None)
        if self.upload_id_marker is not None:
            result['UploadIdMarker'] = self.upload_id_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        self.common_prefixes = []
        if m.get('CommonPrefixes') is not None:
            for k in m.get('CommonPrefixes'):
                temp_model = CommonPrefix()
                self.common_prefixes.append(temp_model.from_map(k))
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('KeyMarker') is not None:
            self.key_marker = m.get('KeyMarker')
        if m.get('MaxUploads') is not None:
            self.max_uploads = m.get('MaxUploads')
        if m.get('NextKeyMarker') is not None:
            self.next_key_marker = m.get('NextKeyMarker')
        if m.get('NextUploadIdMarker') is not None:
            self.next_upload_id_marker = m.get('NextUploadIdMarker')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        self.uploads = []
        if m.get('Upload') is not None:
            for k in m.get('Upload'):
                temp_model = Upload()
                self.uploads.append(temp_model.from_map(k))
        if m.get('UploadIdMarker') is not None:
            self.upload_id_marker = m.get('UploadIdMarker')
        return self


class ListMultipartUploadsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultipartUploadsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListMultipartUploadsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListObjectVersionsRequest(TeaModel):
    def __init__(
        self,
        delimiter: str = None,
        encoding_type: str = None,
        key_marker: str = None,
        max_keys: int = None,
        prefix: str = None,
        version_id_marker: str = None,
    ):
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.key_marker = key_marker
        self.max_keys = max_keys
        self.prefix = prefix
        self.version_id_marker = version_id_marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delimiter is not None:
            result['delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['encoding-type'] = self.encoding_type
        if self.key_marker is not None:
            result['key-marker'] = self.key_marker
        if self.max_keys is not None:
            result['max-keys'] = self.max_keys
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.version_id_marker is not None:
            result['version-id-marker'] = self.version_id_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delimiter') is not None:
            self.delimiter = m.get('delimiter')
        if m.get('encoding-type') is not None:
            self.encoding_type = m.get('encoding-type')
        if m.get('key-marker') is not None:
            self.key_marker = m.get('key-marker')
        if m.get('max-keys') is not None:
            self.max_keys = m.get('max-keys')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('version-id-marker') is not None:
            self.version_id_marker = m.get('version-id-marker')
        return self


class ListObjectVersionsResponseBody(TeaModel):
    def __init__(
        self,
        common_prefixes: List[CommonPrefix] = None,
        delete_markers: List[DeleteMarkerEntry] = None,
        delimiter: str = None,
        encoding_type: str = None,
        is_truncated: bool = None,
        key_marker: str = None,
        max_keys: int = None,
        name: str = None,
        next_key_marker: str = None,
        next_version_id_marker: str = None,
        prefix: str = None,
        versions: List[ObjectVersion] = None,
        version_id_marker: str = None,
    ):
        self.common_prefixes = common_prefixes
        self.delete_markers = delete_markers
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.is_truncated = is_truncated
        self.key_marker = key_marker
        self.max_keys = max_keys
        self.name = name
        self.next_key_marker = next_key_marker
        self.next_version_id_marker = next_version_id_marker
        self.prefix = prefix
        self.versions = versions
        self.version_id_marker = version_id_marker

    def validate(self):
        if self.common_prefixes:
            for k in self.common_prefixes:
                if k:
                    k.validate()
        if self.delete_markers:
            for k in self.delete_markers:
                if k:
                    k.validate()
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommonPrefixes'] = []
        if self.common_prefixes is not None:
            for k in self.common_prefixes:
                result['CommonPrefixes'].append(k.to_map() if k else None)
        result['DeleteMarker'] = []
        if self.delete_markers is not None:
            for k in self.delete_markers:
                result['DeleteMarker'].append(k.to_map() if k else None)
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.key_marker is not None:
            result['KeyMarker'] = self.key_marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.name is not None:
            result['Name'] = self.name
        if self.next_key_marker is not None:
            result['NextKeyMarker'] = self.next_key_marker
        if self.next_version_id_marker is not None:
            result['NextVersionIdMarker'] = self.next_version_id_marker
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        result['Version'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Version'].append(k.to_map() if k else None)
        if self.version_id_marker is not None:
            result['VersionIdMarker'] = self.version_id_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_prefixes = []
        if m.get('CommonPrefixes') is not None:
            for k in m.get('CommonPrefixes'):
                temp_model = CommonPrefix()
                self.common_prefixes.append(temp_model.from_map(k))
        self.delete_markers = []
        if m.get('DeleteMarker') is not None:
            for k in m.get('DeleteMarker'):
                temp_model = DeleteMarkerEntry()
                self.delete_markers.append(temp_model.from_map(k))
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('KeyMarker') is not None:
            self.key_marker = m.get('KeyMarker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextKeyMarker') is not None:
            self.next_key_marker = m.get('NextKeyMarker')
        if m.get('NextVersionIdMarker') is not None:
            self.next_version_id_marker = m.get('NextVersionIdMarker')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        self.versions = []
        if m.get('Version') is not None:
            for k in m.get('Version'):
                temp_model = ObjectVersion()
                self.versions.append(temp_model.from_map(k))
        if m.get('VersionIdMarker') is not None:
            self.version_id_marker = m.get('VersionIdMarker')
        return self


class ListObjectVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListObjectVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListObjectVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListObjectsRequest(TeaModel):
    def __init__(
        self,
        delimiter: str = None,
        encoding_type: str = None,
        marker: str = None,
        max_keys: int = None,
        prefix: str = None,
    ):
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.marker = marker
        self.max_keys = max_keys
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delimiter is not None:
            result['delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['encoding-type'] = self.encoding_type
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['max-keys'] = self.max_keys
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delimiter') is not None:
            self.delimiter = m.get('delimiter')
        if m.get('encoding-type') is not None:
            self.encoding_type = m.get('encoding-type')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('max-keys') is not None:
            self.max_keys = m.get('max-keys')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListObjectsResponseBody(TeaModel):
    def __init__(
        self,
        common_prefixes: List[CommonPrefix] = None,
        contents: List[ObjectSummary] = None,
        delimiter: str = None,
        encoding_type: str = None,
        is_truncated: bool = None,
        marker: str = None,
        max_keys: int = None,
        name: str = None,
        next_marker: str = None,
        prefix: str = None,
    ):
        self.common_prefixes = common_prefixes
        self.contents = contents
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.is_truncated = is_truncated
        self.marker = marker
        self.max_keys = max_keys
        self.name = name
        self.next_marker = next_marker
        self.prefix = prefix

    def validate(self):
        if self.common_prefixes:
            for k in self.common_prefixes:
                if k:
                    k.validate()
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommonPrefixes'] = []
        if self.common_prefixes is not None:
            for k in self.common_prefixes:
                result['CommonPrefixes'].append(k.to_map() if k else None)
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.name is not None:
            result['Name'] = self.name
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_prefixes = []
        if m.get('CommonPrefixes') is not None:
            for k in m.get('CommonPrefixes'):
                temp_model = CommonPrefix()
                self.common_prefixes.append(temp_model.from_map(k))
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = ObjectSummary()
                self.contents.append(temp_model.from_map(k))
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListObjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListObjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListObjectsV2Request(TeaModel):
    def __init__(
        self,
        continuation_token: str = None,
        delimiter: str = None,
        encoding_type: str = None,
        fetch_owner: bool = None,
        max_keys: int = None,
        prefix: str = None,
        start_after: str = None,
    ):
        self.continuation_token = continuation_token
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.fetch_owner = fetch_owner
        self.max_keys = max_keys
        self.prefix = prefix
        self.start_after = start_after

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.continuation_token is not None:
            result['continuation-token'] = self.continuation_token
        if self.delimiter is not None:
            result['delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['encoding-type'] = self.encoding_type
        if self.fetch_owner is not None:
            result['fetch-owner'] = self.fetch_owner
        if self.max_keys is not None:
            result['max-keys'] = self.max_keys
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_after is not None:
            result['start-after'] = self.start_after
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('continuation-token') is not None:
            self.continuation_token = m.get('continuation-token')
        if m.get('delimiter') is not None:
            self.delimiter = m.get('delimiter')
        if m.get('encoding-type') is not None:
            self.encoding_type = m.get('encoding-type')
        if m.get('fetch-owner') is not None:
            self.fetch_owner = m.get('fetch-owner')
        if m.get('max-keys') is not None:
            self.max_keys = m.get('max-keys')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('start-after') is not None:
            self.start_after = m.get('start-after')
        return self


class ListObjectsV2ResponseBody(TeaModel):
    def __init__(
        self,
        common_prefixes: List[CommonPrefix] = None,
        contents: List[ObjectSummary] = None,
        continuation_token: str = None,
        delimiter: str = None,
        encoding_type: str = None,
        is_truncated: bool = None,
        key_count: int = None,
        max_keys: int = None,
        name: str = None,
        next_continuation_token: str = None,
        prefix: str = None,
        start_after: str = None,
    ):
        self.common_prefixes = common_prefixes
        self.contents = contents
        self.continuation_token = continuation_token
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.is_truncated = is_truncated
        self.key_count = key_count
        self.max_keys = max_keys
        self.name = name
        self.next_continuation_token = next_continuation_token
        self.prefix = prefix
        self.start_after = start_after

    def validate(self):
        if self.common_prefixes:
            for k in self.common_prefixes:
                if k:
                    k.validate()
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommonPrefixes'] = []
        if self.common_prefixes is not None:
            for k in self.common_prefixes:
                result['CommonPrefixes'].append(k.to_map() if k else None)
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.key_count is not None:
            result['KeyCount'] = self.key_count
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.name is not None:
            result['Name'] = self.name
        if self.next_continuation_token is not None:
            result['NextContinuationToken'] = self.next_continuation_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.start_after is not None:
            result['StartAfter'] = self.start_after
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_prefixes = []
        if m.get('CommonPrefixes') is not None:
            for k in m.get('CommonPrefixes'):
                temp_model = CommonPrefix()
                self.common_prefixes.append(temp_model.from_map(k))
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = ObjectSummary()
                self.contents.append(temp_model.from_map(k))
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('KeyCount') is not None:
            self.key_count = m.get('KeyCount')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextContinuationToken') is not None:
            self.next_continuation_token = m.get('NextContinuationToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('StartAfter') is not None:
            self.start_after = m.get('StartAfter')
        return self


class ListObjectsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListObjectsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListObjectsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPartsRequest(TeaModel):
    def __init__(
        self,
        encoding_type: str = None,
        max_parts: int = None,
        part_number_marker: int = None,
        upload_id: str = None,
    ):
        self.encoding_type = encoding_type
        self.max_parts = max_parts
        self.part_number_marker = part_number_marker
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encoding_type is not None:
            result['encoding-type'] = self.encoding_type
        if self.max_parts is not None:
            result['max-parts'] = self.max_parts
        if self.part_number_marker is not None:
            result['part-number-marker'] = self.part_number_marker
        if self.upload_id is not None:
            result['uploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encoding-type') is not None:
            self.encoding_type = m.get('encoding-type')
        if m.get('max-parts') is not None:
            self.max_parts = m.get('max-parts')
        if m.get('part-number-marker') is not None:
            self.part_number_marker = m.get('part-number-marker')
        if m.get('uploadId') is not None:
            self.upload_id = m.get('uploadId')
        return self


class ListPartsShrinkRequest(TeaModel):
    def __init__(
        self,
        encoding_type_shrink: str = None,
        max_parts: int = None,
        part_number_marker: int = None,
        upload_id: str = None,
    ):
        self.encoding_type_shrink = encoding_type_shrink
        self.max_parts = max_parts
        self.part_number_marker = part_number_marker
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encoding_type_shrink is not None:
            result['encoding-type'] = self.encoding_type_shrink
        if self.max_parts is not None:
            result['max-parts'] = self.max_parts
        if self.part_number_marker is not None:
            result['part-number-marker'] = self.part_number_marker
        if self.upload_id is not None:
            result['uploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encoding-type') is not None:
            self.encoding_type_shrink = m.get('encoding-type')
        if m.get('max-parts') is not None:
            self.max_parts = m.get('max-parts')
        if m.get('part-number-marker') is not None:
            self.part_number_marker = m.get('part-number-marker')
        if m.get('uploadId') is not None:
            self.upload_id = m.get('uploadId')
        return self


class ListPartsResponseBody(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        is_truncated: bool = None,
        key: str = None,
        max_parts: int = None,
        next_part_number_marker: int = None,
        part: List[Part] = None,
        part_number_marker: int = None,
        upload_id: str = None,
    ):
        self.bucket = bucket
        self.is_truncated = is_truncated
        self.key = key
        self.max_parts = max_parts
        self.next_part_number_marker = next_part_number_marker
        self.part = part
        self.part_number_marker = part_number_marker
        self.upload_id = upload_id

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.key is not None:
            result['Key'] = self.key
        if self.max_parts is not None:
            result['MaxParts'] = self.max_parts
        if self.next_part_number_marker is not None:
            result['NextPartNumberMarker'] = self.next_part_number_marker
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.part_number_marker is not None:
            result['PartNumberMarker'] = self.part_number_marker
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MaxParts') is not None:
            self.max_parts = m.get('MaxParts')
        if m.get('NextPartNumberMarker') is not None:
            self.next_part_number_marker = m.get('NextPartNumberMarker')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = Part()
                self.part.append(temp_model.from_map(k))
        if m.get('PartNumberMarker') is not None:
            self.part_number_marker = m.get('PartNumberMarker')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        return self


class ListPartsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPartsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListPartsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OptionObjectHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        access_control_request_headers: str = None,
        access_control_request_method: str = None,
        origin: str = None,
    ):
        self.common_headers = common_headers
        self.access_control_request_headers = access_control_request_headers
        self.access_control_request_method = access_control_request_method
        self.origin = origin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.access_control_request_headers is not None:
            result['Access-Control-Request-Headers'] = self.access_control_request_headers
        if self.access_control_request_method is not None:
            result['Access-Control-Request-Method'] = self.access_control_request_method
        if self.origin is not None:
            result['Origin'] = self.origin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Access-Control-Request-Headers') is not None:
            self.access_control_request_headers = m.get('Access-Control-Request-Headers')
        if m.get('Access-Control-Request-Method') is not None:
            self.access_control_request_method = m.get('Access-Control-Request-Method')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        return self


class OptionObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PostObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PostVodPlaylistRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class PostVodPlaylistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        acl: str = None,
    ):
        self.common_headers = common_headers
        self.acl = acl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.acl is not None:
            result['x-oss-acl'] = self.acl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-oss-acl') is not None:
            self.acl = m.get('x-oss-acl')
        return self


class PutBucketRequest(TeaModel):
    def __init__(
        self,
        create_bucket_configuration: CreateBucketConfiguration = None,
    ):
        self.create_bucket_configuration = create_bucket_configuration

    def validate(self):
        if self.create_bucket_configuration:
            self.create_bucket_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_bucket_configuration is not None:
            result['CreateBucketConfiguration'] = self.create_bucket_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateBucketConfiguration') is not None:
            temp_model = CreateBucketConfiguration()
            self.create_bucket_configuration = temp_model.from_map(m['CreateBucketConfiguration'])
        return self


class PutBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketAclHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        acl: str = None,
    ):
        self.common_headers = common_headers
        self.acl = acl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.acl is not None:
            result['x-oss-acl'] = self.acl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-oss-acl') is not None:
            self.acl = m.get('x-oss-acl')
        return self


class PutBucketAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketCorsRequest(TeaModel):
    def __init__(
        self,
        c_orsconfiguration: CORSConfiguration = None,
    ):
        self.c_orsconfiguration = c_orsconfiguration

    def validate(self):
        if self.c_orsconfiguration:
            self.c_orsconfiguration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.c_orsconfiguration is not None:
            result['CORSConfiguration'] = self.c_orsconfiguration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CORSConfiguration') is not None:
            temp_model = CORSConfiguration()
            self.c_orsconfiguration = temp_model.from_map(m['CORSConfiguration'])
        return self


class PutBucketCorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketEncryptionRequest(TeaModel):
    def __init__(
        self,
        server_side_encryption_rule: ServerSideEncryptionRule = None,
    ):
        self.server_side_encryption_rule = server_side_encryption_rule

    def validate(self):
        if self.server_side_encryption_rule:
            self.server_side_encryption_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_side_encryption_rule is not None:
            result['ServerSideEncryptionRule'] = self.server_side_encryption_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerSideEncryptionRule') is not None:
            temp_model = ServerSideEncryptionRule()
            self.server_side_encryption_rule = temp_model.from_map(m['ServerSideEncryptionRule'])
        return self


class PutBucketEncryptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketInventoryRequest(TeaModel):
    def __init__(
        self,
        inventory_configuration: InventoryConfiguration = None,
        inventory_id: str = None,
    ):
        self.inventory_configuration = inventory_configuration
        self.inventory_id = inventory_id

    def validate(self):
        if self.inventory_configuration:
            self.inventory_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory_configuration is not None:
            result['InventoryConfiguration'] = self.inventory_configuration.to_map()
        if self.inventory_id is not None:
            result['inventoryId'] = self.inventory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InventoryConfiguration') is not None:
            temp_model = InventoryConfiguration()
            self.inventory_configuration = temp_model.from_map(m['InventoryConfiguration'])
        if m.get('inventoryId') is not None:
            self.inventory_id = m.get('inventoryId')
        return self


class PutBucketInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketLifecycleRequest(TeaModel):
    def __init__(
        self,
        lifecycle_configuration: LifecycleConfiguration = None,
    ):
        self.lifecycle_configuration = lifecycle_configuration

    def validate(self):
        if self.lifecycle_configuration:
            self.lifecycle_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle_configuration is not None:
            result['LifecycleConfiguration'] = self.lifecycle_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LifecycleConfiguration') is not None:
            temp_model = LifecycleConfiguration()
            self.lifecycle_configuration = temp_model.from_map(m['LifecycleConfiguration'])
        return self


class PutBucketLifecycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketLoggingRequest(TeaModel):
    def __init__(
        self,
        bucket_logging_status: BucketLoggingStatus = None,
    ):
        self.bucket_logging_status = bucket_logging_status

    def validate(self):
        if self.bucket_logging_status:
            self.bucket_logging_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_logging_status is not None:
            result['BucketLoggingStatus'] = self.bucket_logging_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketLoggingStatus') is not None:
            temp_model = BucketLoggingStatus()
            self.bucket_logging_status = temp_model.from_map(m['BucketLoggingStatus'])
        return self


class PutBucketLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketPolicyRequest(TeaModel):
    def __init__(
        self,
        policy: str = None,
    ):
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['body'] = self.policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.policy = m.get('body')
        return self


class PutBucketPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketRefererRequest(TeaModel):
    def __init__(
        self,
        referer_configuration: RefererConfiguration = None,
    ):
        self.referer_configuration = referer_configuration

    def validate(self):
        if self.referer_configuration:
            self.referer_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.referer_configuration is not None:
            result['RefererConfiguration'] = self.referer_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefererConfiguration') is not None:
            temp_model = RefererConfiguration()
            self.referer_configuration = temp_model.from_map(m['RefererConfiguration'])
        return self


class PutBucketRefererResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketReplicationRequest(TeaModel):
    def __init__(
        self,
        replication_configuration: ReplicationConfiguration = None,
    ):
        self.replication_configuration = replication_configuration

    def validate(self):
        if self.replication_configuration:
            self.replication_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.replication_configuration is not None:
            result['ReplicationConfiguration'] = self.replication_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReplicationConfiguration') is not None:
            temp_model = ReplicationConfiguration()
            self.replication_configuration = temp_model.from_map(m['ReplicationConfiguration'])
        return self


class PutBucketReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketRequestPaymentRequest(TeaModel):
    def __init__(
        self,
        request_payment_configuration: RequestPaymentConfiguration = None,
    ):
        self.request_payment_configuration = request_payment_configuration

    def validate(self):
        if self.request_payment_configuration:
            self.request_payment_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_payment_configuration is not None:
            result['RequestPaymentConfiguration'] = self.request_payment_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPaymentConfiguration') is not None:
            temp_model = RequestPaymentConfiguration()
            self.request_payment_configuration = temp_model.from_map(m['RequestPaymentConfiguration'])
        return self


class PutBucketRequestPaymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketTagsRequest(TeaModel):
    def __init__(
        self,
        tagging: Tagging = None,
    ):
        self.tagging = tagging

    def validate(self):
        if self.tagging:
            self.tagging.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tagging is not None:
            result['Tagging'] = self.tagging.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tagging') is not None:
            temp_model = Tagging()
            self.tagging = temp_model.from_map(m['Tagging'])
        return self


class PutBucketTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketTransferAccelerationRequest(TeaModel):
    def __init__(
        self,
        transfer_acceleration_configuration: TransferAccelerationConfiguration = None,
    ):
        self.transfer_acceleration_configuration = transfer_acceleration_configuration

    def validate(self):
        if self.transfer_acceleration_configuration:
            self.transfer_acceleration_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transfer_acceleration_configuration is not None:
            result['TransferAccelerationConfiguration'] = self.transfer_acceleration_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransferAccelerationConfiguration') is not None:
            temp_model = TransferAccelerationConfiguration()
            self.transfer_acceleration_configuration = temp_model.from_map(m['TransferAccelerationConfiguration'])
        return self


class PutBucketTransferAccelerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketVersioningRequest(TeaModel):
    def __init__(
        self,
        versioning_configuration: VersioningConfiguration = None,
    ):
        self.versioning_configuration = versioning_configuration

    def validate(self):
        if self.versioning_configuration:
            self.versioning_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.versioning_configuration is not None:
            result['VersioningConfiguration'] = self.versioning_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersioningConfiguration') is not None:
            temp_model = VersioningConfiguration()
            self.versioning_configuration = temp_model.from_map(m['VersioningConfiguration'])
        return self


class PutBucketVersioningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutBucketWebsiteRequest(TeaModel):
    def __init__(
        self,
        website_configuration: WebsiteConfiguration = None,
    ):
        self.website_configuration = website_configuration

    def validate(self):
        if self.website_configuration:
            self.website_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.website_configuration is not None:
            result['WebsiteConfiguration'] = self.website_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebsiteConfiguration') is not None:
            temp_model = WebsiteConfiguration()
            self.website_configuration = temp_model.from_map(m['WebsiteConfiguration'])
        return self


class PutBucketWebsiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutLiveChannelRequest(TeaModel):
    def __init__(
        self,
        live_channel_configuration: LiveChannelConfiguration = None,
    ):
        self.live_channel_configuration = live_channel_configuration

    def validate(self):
        if self.live_channel_configuration:
            self.live_channel_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_channel_configuration is not None:
            result['LiveChannelConfiguration'] = self.live_channel_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveChannelConfiguration') is not None:
            temp_model = LiveChannelConfiguration()
            self.live_channel_configuration = temp_model.from_map(m['LiveChannelConfiguration'])
        return self


class PutLiveChannelResponseBody(TeaModel):
    def __init__(
        self,
        play_urls: LiveChannelPlayUrls = None,
        publish_urls: LiveChannelPublishUrls = None,
    ):
        self.play_urls = play_urls
        self.publish_urls = publish_urls

    def validate(self):
        if self.play_urls:
            self.play_urls.validate()
        if self.publish_urls:
            self.publish_urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.play_urls is not None:
            result['PlayUrls'] = self.play_urls.to_map()
        if self.publish_urls is not None:
            result['PublishUrls'] = self.publish_urls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlayUrls') is not None:
            temp_model = LiveChannelPlayUrls()
            self.play_urls = temp_model.from_map(m['PlayUrls'])
        if m.get('PublishUrls') is not None:
            temp_model = LiveChannelPublishUrls()
            self.publish_urls = temp_model.from_map(m['PublishUrls'])
        return self


class PutLiveChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutLiveChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PutLiveChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutLiveChannelStatusRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class PutLiveChannelStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutObjectHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        forbid_overwrite: bool = None,
        meta_data: Dict[str, str] = None,
        acl: str = None,
        sse_data_encryption: str = None,
        server_side_encryption: str = None,
        sse_key_id: str = None,
        storage_class: str = None,
        tagging: str = None,
    ):
        self.common_headers = common_headers
        self.forbid_overwrite = forbid_overwrite
        self.meta_data = meta_data
        self.acl = acl
        self.sse_data_encryption = sse_data_encryption
        self.server_side_encryption = server_side_encryption
        self.sse_key_id = sse_key_id
        self.storage_class = storage_class
        self.tagging = tagging

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.forbid_overwrite is not None:
            result['x-oss-forbid-overwrite'] = self.forbid_overwrite
        if self.meta_data is not None:
            result['x-oss-meta-*'] = self.meta_data
        if self.acl is not None:
            result['x-oss-object-acl'] = self.acl
        if self.sse_data_encryption is not None:
            result['x-oss-server-side-data-encryption'] = self.sse_data_encryption
        if self.server_side_encryption is not None:
            result['x-oss-server-side-encryption'] = self.server_side_encryption
        if self.sse_key_id is not None:
            result['x-oss-server-side-encryption-key-id'] = self.sse_key_id
        if self.storage_class is not None:
            result['x-oss-storage-class'] = self.storage_class
        if self.tagging is not None:
            result['x-oss-tagging'] = self.tagging
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-oss-forbid-overwrite') is not None:
            self.forbid_overwrite = m.get('x-oss-forbid-overwrite')
        if m.get('x-oss-meta-*') is not None:
            self.meta_data = m.get('x-oss-meta-*')
        if m.get('x-oss-object-acl') is not None:
            self.acl = m.get('x-oss-object-acl')
        if m.get('x-oss-server-side-data-encryption') is not None:
            self.sse_data_encryption = m.get('x-oss-server-side-data-encryption')
        if m.get('x-oss-server-side-encryption') is not None:
            self.server_side_encryption = m.get('x-oss-server-side-encryption')
        if m.get('x-oss-server-side-encryption-key-id') is not None:
            self.sse_key_id = m.get('x-oss-server-side-encryption-key-id')
        if m.get('x-oss-storage-class') is not None:
            self.storage_class = m.get('x-oss-storage-class')
        if m.get('x-oss-tagging') is not None:
            self.tagging = m.get('x-oss-tagging')
        return self


class PutObjectRequest(TeaModel):
    def __init__(
        self,
        body: BinaryIO = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PutObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutObjectAclHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        acl: str = None,
    ):
        self.common_headers = common_headers
        self.acl = acl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.acl is not None:
            result['x-oss-object-acl'] = self.acl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-oss-object-acl') is not None:
            self.acl = m.get('x-oss-object-acl')
        return self


class PutObjectAclRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class PutObjectAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutObjectTaggingRequest(TeaModel):
    def __init__(
        self,
        tagging: Tagging = None,
        version_id: str = None,
    ):
        self.tagging = tagging
        self.version_id = version_id

    def validate(self):
        if self.tagging:
            self.tagging.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tagging is not None:
            result['Tagging'] = self.tagging.to_map()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tagging') is not None:
            temp_model = Tagging()
            self.tagging = temp_model.from_map(m['Tagging'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class PutObjectTaggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutSymlinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        forbid_overwrite: str = None,
        acl: str = None,
        storage_class: str = None,
        symlink_target_key: str = None,
    ):
        self.common_headers = common_headers
        self.forbid_overwrite = forbid_overwrite
        self.acl = acl
        self.storage_class = storage_class
        self.symlink_target_key = symlink_target_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.forbid_overwrite is not None:
            result['x-oss-forbid-overwrite'] = self.forbid_overwrite
        if self.acl is not None:
            result['x-oss-object-acl'] = self.acl
        if self.storage_class is not None:
            result['x-oss-storage-class'] = self.storage_class
        if self.symlink_target_key is not None:
            result['x-oss-symlink-target'] = self.symlink_target_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-oss-forbid-overwrite') is not None:
            self.forbid_overwrite = m.get('x-oss-forbid-overwrite')
        if m.get('x-oss-object-acl') is not None:
            self.acl = m.get('x-oss-object-acl')
        if m.get('x-oss-storage-class') is not None:
            self.storage_class = m.get('x-oss-storage-class')
        if m.get('x-oss-symlink-target') is not None:
            self.symlink_target_key = m.get('x-oss-symlink-target')
        return self


class PutSymlinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RestoreObjectRequest(TeaModel):
    def __init__(
        self,
        restore_request: RestoreRequest = None,
        version_id: str = None,
    ):
        self.restore_request = restore_request
        self.version_id = version_id

    def validate(self):
        if self.restore_request:
            self.restore_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restore_request is not None:
            result['RestoreRequest'] = self.restore_request.to_map()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreRequest') is not None:
            temp_model = RestoreRequest()
            self.restore_request = temp_model.from_map(m['RestoreRequest'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class RestoreObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class SelectObjectRequest(TeaModel):
    def __init__(
        self,
        select_request: SelectRequest = None,
    ):
        self.select_request = select_request

    def validate(self):
        if self.select_request:
            self.select_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select_request is not None:
            result['SelectRequest'] = self.select_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectRequest') is not None:
            temp_model = SelectRequest()
            self.select_request = temp_model.from_map(m['SelectRequest'])
        return self


class SelectObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BinaryIO = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UploadPartRequest(TeaModel):
    def __init__(
        self,
        body: BinaryIO = None,
        part_number: int = None,
        upload_id: str = None,
    ):
        self.body = body
        self.part_number = part_number
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.part_number is not None:
            result['partNumber'] = self.part_number
        if self.upload_id is not None:
            result['uploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('partNumber') is not None:
            self.part_number = m.get('partNumber')
        if m.get('uploadId') is not None:
            self.upload_id = m.get('uploadId')
        return self


class UploadPartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UploadPartCopyHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        copy_source: str = None,
        copy_source_if_match: str = None,
        copy_source_if_modified_since: str = None,
        copy_source_if_none_match: str = None,
        copy_source_if_unmodified_since: str = None,
        copy_source_range: str = None,
    ):
        self.common_headers = common_headers
        self.copy_source = copy_source
        self.copy_source_if_match = copy_source_if_match
        self.copy_source_if_modified_since = copy_source_if_modified_since
        self.copy_source_if_none_match = copy_source_if_none_match
        self.copy_source_if_unmodified_since = copy_source_if_unmodified_since
        self.copy_source_range = copy_source_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.copy_source is not None:
            result['x-oss-copy-source'] = self.copy_source
        if self.copy_source_if_match is not None:
            result['x-oss-copy-source-if-match'] = self.copy_source_if_match
        if self.copy_source_if_modified_since is not None:
            result['x-oss-copy-source-if-modified-since'] = self.copy_source_if_modified_since
        if self.copy_source_if_none_match is not None:
            result['x-oss-copy-source-if-none-match'] = self.copy_source_if_none_match
        if self.copy_source_if_unmodified_since is not None:
            result['x-oss-copy-source-if-unmodified-since'] = self.copy_source_if_unmodified_since
        if self.copy_source_range is not None:
            result['x-oss-copy-source-range'] = self.copy_source_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-oss-copy-source') is not None:
            self.copy_source = m.get('x-oss-copy-source')
        if m.get('x-oss-copy-source-if-match') is not None:
            self.copy_source_if_match = m.get('x-oss-copy-source-if-match')
        if m.get('x-oss-copy-source-if-modified-since') is not None:
            self.copy_source_if_modified_since = m.get('x-oss-copy-source-if-modified-since')
        if m.get('x-oss-copy-source-if-none-match') is not None:
            self.copy_source_if_none_match = m.get('x-oss-copy-source-if-none-match')
        if m.get('x-oss-copy-source-if-unmodified-since') is not None:
            self.copy_source_if_unmodified_since = m.get('x-oss-copy-source-if-unmodified-since')
        if m.get('x-oss-copy-source-range') is not None:
            self.copy_source_range = m.get('x-oss-copy-source-range')
        return self


class UploadPartCopyRequest(TeaModel):
    def __init__(
        self,
        part_number: int = None,
        upload_id: str = None,
    ):
        self.part_number = part_number
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.part_number is not None:
            result['partNumber'] = self.part_number
        if self.upload_id is not None:
            result['uploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('partNumber') is not None:
            self.part_number = m.get('partNumber')
        if m.get('uploadId') is not None:
            self.upload_id = m.get('uploadId')
        return self


class UploadPartCopyResponseBody(TeaModel):
    def __init__(
        self,
        etag: str = None,
        last_modified: str = None,
    ):
        self.etag = etag
        self.last_modified = last_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class UploadPartCopyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadPartCopyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UploadPartCopyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


