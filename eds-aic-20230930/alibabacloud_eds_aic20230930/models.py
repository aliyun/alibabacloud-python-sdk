# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DataImageRegionDistributeMapValue(TeaModel):
    def __init__(
        self,
        distribute_status: str = None,
        progress: str = None,
    ):
        # The status of the image distribution task.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The task is ready.
        # *   DELETE: The task is deleted.
        # *   INIT: The task is being initialized.
        # *   CREATE_FAILED: The task failed to be created.
        # *   CREATING: The task is being created.
        self.distribute_status = distribute_status
        # The distribution progress of the image.
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribute_status is not None:
            result['DistributeStatus'] = self.distribute_status
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeStatus') is not None:
            self.distribute_status = m.get('DistributeStatus')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class AttachKeyPairRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        key_pair_id: str = None,
    ):
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        self.instance_ids = instance_ids
        # The ID of the ADB key pair.
        # 
        # This parameter is required.
        self.key_pair_id = key_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        return self


class AttachKeyPairResponseBodyData(TeaModel):
    def __init__(
        self,
        attached_instance_ids: List[str] = None,
        fail_count: int = None,
        key_pair_id: str = None,
        total_count: int = None,
    ):
        # The IDs of the cloud phone instances to which the ADB key pair is successfully attached.
        self.attached_instance_ids = attached_instance_ids
        # The number of the cloud phone instances to which the ADB key pair failed to be attached.
        self.fail_count = fail_count
        # The ID of the ADB key pair.
        self.key_pair_id = key_pair_id
        # The total number of the cloud phone instances.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_instance_ids is not None:
            result['AttachedInstanceIds'] = self.attached_instance_ids
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedInstanceIds') is not None:
            self.attached_instance_ids = m.get('AttachedInstanceIds')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class AttachKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        data: AttachKeyPairResponseBodyData = None,
        request_id: str = None,
    ):
        # The object that is returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AttachKeyPairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachKeyPairResponseBody = None,
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
            temp_model = AttachKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        authorize_user_id: str = None,
        un_authorize_user_id: str = None,
    ):
        # List of instance IDs.
        self.android_instance_ids = android_instance_ids
        # User ID to be assigned.
        self.authorize_user_id = authorize_user_id
        # User ID to be unassigned.
        self.un_authorize_user_id = un_authorize_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.authorize_user_id is not None:
            result['AuthorizeUserId'] = self.authorize_user_id
        if self.un_authorize_user_id is not None:
            result['UnAuthorizeUserId'] = self.un_authorize_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('AuthorizeUserId') is not None:
            self.authorize_user_id = m.get('AuthorizeUserId')
        if m.get('UnAuthorizeUserId') is not None:
            self.un_authorize_user_id = m.get('UnAuthorizeUserId')
        return self


class AuthorizeAndroidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeAndroidInstanceResponseBody = None,
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
            temp_model = AuthorizeAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BackupFileRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_all: bool = None,
        backup_file_name: str = None,
        backup_file_path: str = None,
        description: str = None,
        source_app_list: List[str] = None,
        source_file_path_list: List[str] = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # The IDs of the instances.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # Specifies whether to back up the whole instance.
        self.backup_all = backup_all
        # The name of the backup file.
        self.backup_file_name = backup_file_name
        # The OSS path of the backup file.
        # 
        # >  To upload a backup file to an OSS bucket, you must obtain the name of the bucket. When calling the describeBuckets operation to retrieve a bucket name, you must also call the ossObjectList operation to obtain the object key. Combine these to form the full path: oss://${bucketName}/${key}.
        # 
        # This parameter is required.
        self.backup_file_path = backup_file_path
        # The description of the backup file.
        self.description = description
        # The names of the application packages that you want to back up.
        self.source_app_list = source_app_list
        # The paths to the source files.
        self.source_file_path_list = source_file_path_list
        # The endpoint of the OSS bucket to which you want to upload the backup file.
        # 
        # > : When calling the DescribeBuckets operation to query buckets, retrieve the IntranetEndpoint value if the cloud phone and the OSS bucket are in the same region. If they are in different regions, retrieve the ExtranetEndpoint value instead.
        self.upload_endpoint = upload_endpoint
        # The type of the backup.
        # 
        # Valid values:
        # 
        # *   OSS: uploads the backup file to an OSS bucket.
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.backup_all is not None:
            result['BackupAll'] = self.backup_all
        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name
        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path
        if self.description is not None:
            result['Description'] = self.description
        if self.source_app_list is not None:
            result['SourceAppList'] = self.source_app_list
        if self.source_file_path_list is not None:
            result['SourceFilePathList'] = self.source_file_path_list
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('BackupAll') is not None:
            self.backup_all = m.get('BackupAll')
        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')
        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SourceAppList') is not None:
            self.source_app_list = m.get('SourceAppList')
        if m.get('SourceFilePathList') is not None:
            self.source_file_path_list = m.get('SourceFilePathList')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class BackupFileResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        task_id: str = None,
    ):
        # The ID of the cloud phone instance.
        self.android_instance_id = android_instance_id
        # The ID of the backup file.
        self.backup_file_id = backup_file_id
        # The name of the backup file.
        self.backup_file_name = backup_file_name
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id
        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')
        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BackupFileResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        data: List[BackupFileResponseBodyData] = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The number of instances that are backed up.
        self.count = count
        # The object that is returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # The ID of the batch task.
        self.task_id = task_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = BackupFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BackupFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BackupFileResponseBody = None,
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
            temp_model = BackupFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetAcpConnectionTicketRequestInstanceTasks(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
    ):
        # The ID of the cloud phone instance.
        self.instance_id = instance_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BatchGetAcpConnectionTicketRequest(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        instance_group_id: str = None,
        instance_ids: List[str] = None,
        instance_tasks: List[BatchGetAcpConnectionTicketRequestInstanceTasks] = None,
    ):
        # The ID of the user to whom the cloud phone instance is assigned.
        self.end_user_id = end_user_id
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The IDs of the cloud phone instances. You can specify 1 to 100 IDs of cloud phone instances.
        self.instance_ids = instance_ids
        # The instance connection tasks.
        self.instance_tasks = instance_tasks

    def validate(self):
        if self.instance_tasks:
            for k in self.instance_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        result['InstanceTasks'] = []
        if self.instance_tasks is not None:
            for k in self.instance_tasks:
                result['InstanceTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        self.instance_tasks = []
        if m.get('InstanceTasks') is not None:
            for k in m.get('InstanceTasks'):
                temp_model = BatchGetAcpConnectionTicketRequestInstanceTasks()
                self.instance_tasks.append(temp_model.from_map(k))
        return self


class BatchGetAcpConnectionTicketResponseBodyInstanceConnectionModels(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        error_code: str = None,
        instance_id: str = None,
        persistent_app_instance_id: str = None,
        task_id: str = None,
        task_status: str = None,
        ticket: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.error_code = error_code
        # The ID of the cloud phone instance.
        self.instance_id = instance_id
        self.persistent_app_instance_id = persistent_app_instance_id
        # The ID of the task.
        self.task_id = task_id
        # The state of the task.
        self.task_status = task_status
        # The ticket used to connect to the cloud phone instance.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.persistent_app_instance_id is not None:
            result['PersistentAppInstanceId'] = self.persistent_app_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PersistentAppInstanceId') is not None:
            self.persistent_app_instance_id = m.get('PersistentAppInstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class BatchGetAcpConnectionTicketResponseBody(TeaModel):
    def __init__(
        self,
        instance_connection_models: List[BatchGetAcpConnectionTicketResponseBodyInstanceConnectionModels] = None,
        request_id: str = None,
    ):
        # The results of the instance connection tasks.
        self.instance_connection_models = instance_connection_models
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_connection_models:
            for k in self.instance_connection_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceConnectionModels'] = []
        if self.instance_connection_models is not None:
            for k in self.instance_connection_models:
                result['InstanceConnectionModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_connection_models = []
        if m.get('InstanceConnectionModels') is not None:
            for k in m.get('InstanceConnectionModels'):
                temp_model = BatchGetAcpConnectionTicketResponseBodyInstanceConnectionModels()
                self.instance_connection_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetAcpConnectionTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetAcpConnectionTicketResponseBody = None,
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
            temp_model = BatchGetAcpConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeCloudPhoneNodeRequest(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        node_id: str = None,
        phone_count: int = None,
    ):
        self.instance_type = instance_type
        self.node_id = node_id
        self.phone_count = phone_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')
        return self


class ChangeCloudPhoneNodeResponseBodyNodeInfosInstanceInfos(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ChangeCloudPhoneNodeResponseBodyNodeInfos(TeaModel):
    def __init__(
        self,
        instance_infos: List[ChangeCloudPhoneNodeResponseBodyNodeInfosInstanceInfos] = None,
        node_id: str = None,
    ):
        self.instance_infos = instance_infos
        self.node_id = node_id

    def validate(self):
        if self.instance_infos:
            for k in self.instance_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceInfos'] = []
        if self.instance_infos is not None:
            for k in self.instance_infos:
                result['InstanceInfos'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_infos = []
        if m.get('InstanceInfos') is not None:
            for k in m.get('InstanceInfos'):
                temp_model = ChangeCloudPhoneNodeResponseBodyNodeInfosInstanceInfos()
                self.instance_infos.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ChangeCloudPhoneNodeResponseBody(TeaModel):
    def __init__(
        self,
        node_infos: List[ChangeCloudPhoneNodeResponseBodyNodeInfos] = None,
        request_id: str = None,
    ):
        self.node_infos = node_infos
        self.request_id = request_id

    def validate(self):
        if self.node_infos:
            for k in self.node_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInfos'] = []
        if self.node_infos is not None:
            for k in self.node_infos:
                result['NodeInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_infos = []
        if m.get('NodeInfos') is not None:
            for k in m.get('NodeInfos'):
                temp_model = ChangeCloudPhoneNodeResponseBodyNodeInfos()
                self.node_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeCloudPhoneNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeCloudPhoneNodeResponseBody = None,
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
            temp_model = ChangeCloudPhoneNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckResourceStockRequest(TeaModel):
    def __init__(
        self,
        acp_spec_id: str = None,
        amount: int = None,
        biz_region_id: str = None,
        gpu_acceleration: bool = None,
        zone_id: str = None,
    ):
        # Specification ID.
        self.acp_spec_id = acp_spec_id
        self.amount = amount
        # Region ID.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        self.gpu_acceleration = gpu_acceleration
        # The availability zone of the resource.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acp_spec_id is not None:
            result['AcpSpecId'] = self.acp_spec_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcpSpecId') is not None:
            self.acp_spec_id = m.get('AcpSpecId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckResourceStockResponseBodyResourceStockModels(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stock_status: str = None,
        zone_id: str = None,
    ):
        # Region ID.
        self.region_id = region_id
        # Inventory status of the instance group.
        self.stock_status = stock_status
        # Zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stock_status is not None:
            result['StockStatus'] = self.stock_status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StockStatus') is not None:
            self.stock_status = m.get('StockStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckResourceStockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_stock_models: List[CheckResourceStockResponseBodyResourceStockModels] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Details of resource inventory.
        self.resource_stock_models = resource_stock_models

    def validate(self):
        if self.resource_stock_models:
            for k in self.resource_stock_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceStockModels'] = []
        if self.resource_stock_models is not None:
            for k in self.resource_stock_models:
                result['ResourceStockModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_stock_models = []
        if m.get('ResourceStockModels') is not None:
            for k in m.get('ResourceStockModels'):
                temp_model = CheckResourceStockResponseBodyResourceStockModels()
                self.resource_stock_models.append(temp_model.from_map(k))
        return self


class CheckResourceStockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckResourceStockResponseBody = None,
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
            temp_model = CheckResourceStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAndroidInstanceGroupRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class CreateAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_type: str = None,
        client_token: str = None,
        enable_ipv_6: bool = None,
        gpu_acceleration: bool = None,
        image_id: str = None,
        instance_group_name: str = None,
        instance_group_spec: str = None,
        ipv_6bandwidth: int = None,
        key_pair_id: str = None,
        number_of_instances: int = None,
        office_site_id: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        tag: List[CreateAndroidInstanceGroupRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The number of instance groups. Default value: 1. Maximum value: 1.
        self.amount = amount
        # Specifies whether to enable automatic payment. Default value: false.
        # 
        # Valid values:
        # 
        # *   true: enables automatic payment. Make sure that your Alibaba Cloud account has sufficient balance.
        # *   false: disables automatic payment. You must manually complete the payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Default value: false.
        # 
        # Valid values:
        # 
        # *   true: automatically renew resource upon expiration.
        # *   false: manually renew resources upon expiration.
        self.auto_renew = auto_renew
        # The ID of the region. You can call the DescribeRegions operation to query the regions where Cloud Phone is supported.
        # 
        # Valid values:
        # 
        # *   cn-shenzhen: China (Shenzhen).
        # *   cn-beijing: China (Beijing).
        # *   cn-shanghai: China (Shanghai).
        # *   cn-hongkong: China (Hong Kong).
        # *   ap-southeast-1: Singapore.
        # *   cn-hangzhou: China (Hangzhou).
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. The value cannot exceed 100 characters in length.
        self.client_token = client_token
        # >  This parameter is not publicly available.
        self.enable_ipv_6 = enable_ipv_6
        # Specifies whether to enable GPU acceleration.
        # 
        # Valid values:
        # 
        # *   true: enables GPU acceleration.
        # *   false (default): disables GPU acceleration.
        self.gpu_acceleration = gpu_acceleration
        # The ID of the image. You can call the [DescribeImageList](https://help.aliyun.com/document_detail/2807324.html) operation to query images.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The name of the instance group.
        # 
        # >  The name can be up to 30 characters in length. It can contain letters, digits, colons (:), underscores (_), periods (.), or hyphens (-). It must start with letters but cannot start with `http://` or `https://`.
        self.instance_group_name = instance_group_name
        # The specifications of the instance group. You can call the [DescribeSpec](https://help.aliyun.com/document_detail/2807299.html) operation to query the available specifications.
        # 
        # Valid values:
        # 
        # *   acp.perf.large: Performance (8 vCPUs, 16 GiB of memory, and 32 GiB of storage.
        # *   acp.basic.small: Lightweight (2 vCPUs, 4 GiB of memory, and 32 GiB of storage).
        # *   acp.std.large: Standard (4 vCPUs, 8 GiB of memory, and 32 GiB of storage).
        # 
        # This parameter is required.
        self.instance_group_spec = instance_group_spec
        # >  This parameter is not publicly available.
        self.ipv_6bandwidth = ipv_6bandwidth
        # The ID of the key pair. When you create an instance group and specify a valid key pair ID, all cloud phone instances within the group will automatically be bound to that key pair upon creation. This eliminates the need to manually bind key pairs to individual cloud phone instances.
        # 
        # >  Binding key pairs to cloud phone instances is currently not supported during instance group resizing.
        self.key_pair_id = key_pair_id
        # The number of cloud phones in the instance group. Maximum value: 100.
        self.number_of_instances = number_of_instances
        # The ID of the network.
        # 
        # *   This parameter is required if you assign a shared network to cloud phones. You can go to the [Network](https://wya.wuying.aliyun.com/network) page of the Cloud Phone console to retrieve the ID of a **shared network**. If no shared network is available in the Cloud Phone console, you can leave this parameter empty. The system automatically creates one when you create an instance group.
        # *   This parameter is required if you assign a virtual private cloud (VPC) to cloud phones. You can go to the [Network](https://wya.wuying.aliyun.com/network) page of the Cloud Phone console to retrieve the ID of a **VPC**. If no VPC is available in the Cloud Phone console, you must first create one.
        self.office_site_id = office_site_id
        # The subscription duration. The unit is specified by PeriodUnit.
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Hour (Note that this unit is supported only by pay-as-you-go.)
        self.period_unit = period_unit
        # The ID of the policy. You can call the [ListPolicyGroups](https://help.aliyun.com/document_detail/2807352.html) operation to query policies.
        self.policy_group_id = policy_group_id
        # The tags
        self.tag = tag
        # The ID of the vSwitch. You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/448774.html) operation to query vSwitches.
        # 
        # *   This parameter is not required if you assign a shared network to cloud phones.
        # *   This parameter is required if you assign a VPC to cloud phones. The vSwitch specified by this parameter is used to create cloud phones.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6
        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name
        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec
        if self.ipv_6bandwidth is not None:
            result['Ipv6Bandwidth'] = self.ipv_6bandwidth
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.number_of_instances is not None:
            result['NumberOfInstances'] = self.number_of_instances
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')
        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')
        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')
        if m.get('Ipv6Bandwidth') is not None:
            self.ipv_6bandwidth = m.get('Ipv6Bandwidth')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('NumberOfInstances') is not None:
            self.number_of_instances = m.get('NumberOfInstances')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateAndroidInstanceGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos(TeaModel):
    def __init__(
        self,
        instance_group_id: str = None,
        instance_ids: List[str] = None,
    ):
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The IDs of the instances.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class CreateAndroidInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        instance_group_ids: List[str] = None,
        instance_group_infos: List[CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The instance groups.
        self.instance_group_infos = instance_group_infos
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_group_infos:
            for k in self.instance_group_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        result['InstanceGroupInfos'] = []
        if self.instance_group_infos is not None:
            for k in self.instance_group_infos:
                result['InstanceGroupInfos'].append(k.to_map() if k else None)
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        self.instance_group_infos = []
        if m.get('InstanceGroupInfos') is not None:
            for k in m.get('InstanceGroupInfos'):
                temp_model = CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos()
                self.instance_group_infos.append(temp_model.from_map(k))
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAndroidInstanceGroupResponseBody = None,
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
            temp_model = CreateAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequestCustomAppInfo(TeaModel):
    def __init__(
        self,
        apk_size: str = None,
        download_url: str = None,
        md_5: str = None,
        package_name: str = None,
        version: str = None,
        version_code: str = None,
    ):
        # The size of the .apk file. Unit: MB.
        self.apk_size = apk_size
        # The download URL of the app.
        self.download_url = download_url
        # The MD5 value of the .apk file.
        self.md_5 = md_5
        # The name of the app package.
        self.package_name = package_name
        # The version of the app.
        self.version = version
        # The code of the app version.
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apk_size is not None:
            result['ApkSize'] = self.apk_size
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.version is not None:
            result['Version'] = self.version
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApkSize') is not None:
            self.apk_size = m.get('ApkSize')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        biz_region_id: str = None,
        custom_app_info: CreateAppRequestCustomAppInfo = None,
        description: str = None,
        file_name: str = None,
        file_path: str = None,
        icon_url: str = None,
        install_param: str = None,
        oss_app_url: str = None,
        sign_apk: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The ID of the region.
        self.biz_region_id = biz_region_id
        # The information about the custom app.
        # 
        # > 
        # 
        # *   If you want to pass in a custom app, configure the `CustomAppInfo` parameter. Take note that the six fields within it are mandatory.
        # 
        # *   A custom app has a higher priority than an app from the Alibaba Cloud Workspace Application Center. If you configure the `CustomAppInfo` parameter, the `FileName` and `FilePath` pair or the `OssAppUrl` will not take effect.
        self.custom_app_info = custom_app_info
        # The description of the application.
        self.description = description
        # The name used by the app file in Object Storage Service (OSS). This parameter, combined with `FilePath`, uniquely identifies the OSS path of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [Elastic Desktop Service (EDS) Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.file_name = file_name
        # The OSS bucket path to the app file. This parameter, combined with `FileName`, uniquely identifies the OSS path of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [EDS Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.file_path = file_path
        # The icon URL of the application.
        self.icon_url = icon_url
        # The parameters used for installing the application. By default, the `-r` parameter is included when you install an application.
        self.install_param = install_param
        # The OSS bucket endpoint of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [EDS Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.oss_app_url = oss_app_url
        self.sign_apk = sign_apk

    def validate(self):
        if self.custom_app_info:
            self.custom_app_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.custom_app_info is not None:
            result['CustomAppInfo'] = self.custom_app_info.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.install_param is not None:
            result['InstallParam'] = self.install_param
        if self.oss_app_url is not None:
            result['OssAppUrl'] = self.oss_app_url
        if self.sign_apk is not None:
            result['SignApk'] = self.sign_apk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('CustomAppInfo') is not None:
            temp_model = CreateAppRequestCustomAppInfo()
            self.custom_app_info = temp_model.from_map(m['CustomAppInfo'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('InstallParam') is not None:
            self.install_param = m.get('InstallParam')
        if m.get('OssAppUrl') is not None:
            self.oss_app_url = m.get('OssAppUrl')
        if m.get('SignApk') is not None:
            self.sign_apk = m.get('SignApk')
        return self


class CreateAppShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        biz_region_id: str = None,
        custom_app_info_shrink: str = None,
        description: str = None,
        file_name: str = None,
        file_path: str = None,
        icon_url: str = None,
        install_param: str = None,
        oss_app_url: str = None,
        sign_apk: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The ID of the region.
        self.biz_region_id = biz_region_id
        # The information about the custom app.
        # 
        # > 
        # 
        # *   If you want to pass in a custom app, configure the `CustomAppInfo` parameter. Take note that the six fields within it are mandatory.
        # 
        # *   A custom app has a higher priority than an app from the Alibaba Cloud Workspace Application Center. If you configure the `CustomAppInfo` parameter, the `FileName` and `FilePath` pair or the `OssAppUrl` will not take effect.
        self.custom_app_info_shrink = custom_app_info_shrink
        # The description of the application.
        self.description = description
        # The name used by the app file in Object Storage Service (OSS). This parameter, combined with `FilePath`, uniquely identifies the OSS path of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [Elastic Desktop Service (EDS) Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.file_name = file_name
        # The OSS bucket path to the app file. This parameter, combined with `FileName`, uniquely identifies the OSS path of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [EDS Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.file_path = file_path
        # The icon URL of the application.
        self.icon_url = icon_url
        # The parameters used for installing the application. By default, the `-r` parameter is included when you install an application.
        self.install_param = install_param
        # The OSS bucket endpoint of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [EDS Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.oss_app_url = oss_app_url
        self.sign_apk = sign_apk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.custom_app_info_shrink is not None:
            result['CustomAppInfo'] = self.custom_app_info_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.install_param is not None:
            result['InstallParam'] = self.install_param
        if self.oss_app_url is not None:
            result['OssAppUrl'] = self.oss_app_url
        if self.sign_apk is not None:
            result['SignApk'] = self.sign_apk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('CustomAppInfo') is not None:
            self.custom_app_info_shrink = m.get('CustomAppInfo')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('InstallParam') is not None:
            self.install_param = m.get('InstallParam')
        if m.get('OssAppUrl') is not None:
            self.oss_app_url = m.get('OssAppUrl')
        if m.get('SignApk') is not None:
            self.sign_apk = m.get('SignApk')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        request_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCloudPhoneNodeRequestDisplayConfig(TeaModel):
    def __init__(
        self,
        dpi: int = None,
        fps: int = None,
        lock_resolution: str = None,
    ):
        self.dpi = dpi
        self.fps = fps
        self.lock_resolution = lock_resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dpi is not None:
            result['Dpi'] = self.dpi
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dpi') is not None:
            self.dpi = m.get('Dpi')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        return self


class CreateCloudPhoneNodeRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class CreateCloudPhoneNodeRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_type: str = None,
        count: str = None,
        display_config: CreateCloudPhoneNodeRequestDisplayConfig = None,
        image_id: str = None,
        instance_type: str = None,
        network_id: str = None,
        node_name: str = None,
        period: int = None,
        period_unit: str = None,
        phone_count: int = None,
        resolution_height: int = None,
        resolution_width: int = None,
        server_share_data_volume: int = None,
        server_type: str = None,
        tag: List[CreateCloudPhoneNodeRequestTag] = None,
        v_switch_id: str = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   False (default): You must manually complete the payment in the Alibaba Cloud Expenses and Costs console.
        # *   true: enables the auto-payment feature.
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-renewal feature. In this case, the system automatically renews instances upon expiration.
        # *   false (default): disables the auto-renewal feature. In this case, you need to manually renew instances upon expiration.
        self.auto_renew = auto_renew
        # The region ID.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method. Only the subscription billing method is supported.
        self.charge_type = charge_type
        # The number of cloud phone matrixes you want to purchase.
        self.count = count
        self.display_config = display_config
        # The image ID.
        self.image_id = image_id
        # The instance specification.
        # 
        # Valid values:
        # 
        # *   ac.max: By default, this specification allows up to 25 instances. You can adjust this number by using PhoneCount (Value range: 4 to 40).
        # *   ac.plus: By default, this specification allows up to 40 instances. You can adjust this number by using PhoneCount (Value range: 4 to 40).
        self.instance_type = instance_type
        # The office network ID.
        self.network_id = network_id
        # The name of the cloud phone matrix.
        self.node_name = node_name
        # The subscription duration. The unit is specified by `PeriodUnit`. Valid values:
        # 
        # *   When `PeriodUnit` is set to **year**: 1.
        # *   When `PeriodUnit` is set to **month**: 1, 2, 3, and 6.
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month (default)
        # *   Year
        self.period_unit = period_unit
        # The number of instances per cloud phone matrix.
        self.phone_count = phone_count
        # The resolution height. Unit: pixel.
        self.resolution_height = resolution_height
        # The resolution width. Unit: pixel.
        self.resolution_width = resolution_width
        # The shared storage size Unit: GiB.
        self.server_share_data_volume = server_share_data_volume
        # The matrix specification.
        # 
        # Valid values:
        # 
        # *   cpm.gn6.gx1
        # 
        # This parameter is required.
        self.server_type = server_type
        # The resource tags.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.display_config:
            self.display_config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.count is not None:
            result['Count'] = self.count
        if self.display_config is not None:
            result['DisplayConfig'] = self.display_config.to_map()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.server_share_data_volume is not None:
            result['ServerShareDataVolume'] = self.server_share_data_volume
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DisplayConfig') is not None:
            temp_model = CreateCloudPhoneNodeRequestDisplayConfig()
            self.display_config = temp_model.from_map(m['DisplayConfig'])
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('ServerShareDataVolume') is not None:
            self.server_share_data_volume = m.get('ServerShareDataVolume')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateCloudPhoneNodeRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateCloudPhoneNodeShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class CreateCloudPhoneNodeShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_type: str = None,
        count: str = None,
        display_config_shrink: str = None,
        image_id: str = None,
        instance_type: str = None,
        network_id: str = None,
        node_name: str = None,
        period: int = None,
        period_unit: str = None,
        phone_count: int = None,
        resolution_height: int = None,
        resolution_width: int = None,
        server_share_data_volume: int = None,
        server_type: str = None,
        tag: List[CreateCloudPhoneNodeShrinkRequestTag] = None,
        v_switch_id: str = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   False (default): You must manually complete the payment in the Alibaba Cloud Expenses and Costs console.
        # *   true: enables the auto-payment feature.
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-renewal feature. In this case, the system automatically renews instances upon expiration.
        # *   false (default): disables the auto-renewal feature. In this case, you need to manually renew instances upon expiration.
        self.auto_renew = auto_renew
        # The region ID.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method. Only the subscription billing method is supported.
        self.charge_type = charge_type
        # The number of cloud phone matrixes you want to purchase.
        self.count = count
        self.display_config_shrink = display_config_shrink
        # The image ID.
        self.image_id = image_id
        # The instance specification.
        # 
        # Valid values:
        # 
        # *   ac.max: By default, this specification allows up to 25 instances. You can adjust this number by using PhoneCount (Value range: 4 to 40).
        # *   ac.plus: By default, this specification allows up to 40 instances. You can adjust this number by using PhoneCount (Value range: 4 to 40).
        self.instance_type = instance_type
        # The office network ID.
        self.network_id = network_id
        # The name of the cloud phone matrix.
        self.node_name = node_name
        # The subscription duration. The unit is specified by `PeriodUnit`. Valid values:
        # 
        # *   When `PeriodUnit` is set to **year**: 1.
        # *   When `PeriodUnit` is set to **month**: 1, 2, 3, and 6.
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month (default)
        # *   Year
        self.period_unit = period_unit
        # The number of instances per cloud phone matrix.
        self.phone_count = phone_count
        # The resolution height. Unit: pixel.
        self.resolution_height = resolution_height
        # The resolution width. Unit: pixel.
        self.resolution_width = resolution_width
        # The shared storage size Unit: GiB.
        self.server_share_data_volume = server_share_data_volume
        # The matrix specification.
        # 
        # Valid values:
        # 
        # *   cpm.gn6.gx1
        # 
        # This parameter is required.
        self.server_type = server_type
        # The resource tags.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.count is not None:
            result['Count'] = self.count
        if self.display_config_shrink is not None:
            result['DisplayConfig'] = self.display_config_shrink
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.server_share_data_volume is not None:
            result['ServerShareDataVolume'] = self.server_share_data_volume
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DisplayConfig') is not None:
            self.display_config_shrink = m.get('DisplayConfig')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('ServerShareDataVolume') is not None:
            self.server_share_data_volume = m.get('ServerShareDataVolume')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateCloudPhoneNodeShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateCloudPhoneNodeResponseBodyNodeInfos(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        node_id: str = None,
    ):
        # The IDs of the cloud phone instances.
        self.instance_ids = instance_ids
        # The ID of the cloud phone matrix.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateCloudPhoneNodeResponseBody(TeaModel):
    def __init__(
        self,
        node_infos: List[CreateCloudPhoneNodeResponseBodyNodeInfos] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The cloud phone matrixes.
        self.node_infos = node_infos
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.node_infos:
            for k in self.node_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInfos'] = []
        if self.node_infos is not None:
            for k in self.node_infos:
                result['NodeInfos'].append(k.to_map() if k else None)
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_infos = []
        if m.get('NodeInfos') is not None:
            for k in m.get('NodeInfos'):
                temp_model = CreateCloudPhoneNodeResponseBodyNodeInfos()
                self.node_infos.append(temp_model.from_map(k))
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCloudPhoneNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCloudPhoneNodeResponseBody = None,
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
            temp_model = CreateCloudPhoneNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomImageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        image_name: str = None,
        instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. By default, this parameter is left empty. The token cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the custom image.
        self.description = description
        # The name of the custom image.
        # 
        # This parameter is required.
        self.image_name = image_name
        # The ID of the cloud phone instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateCustomImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        # The ID of the custom image.
        self.image_id = image_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomImageResponseBody = None,
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
            temp_model = CreateCustomImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyPairRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
    ):
        # The name of the key pair. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter but cannot start with http:// or https://.
        # 
        # This parameter is required.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class CreateKeyPairResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
        private_key_body: str = None,
    ):
        # The time when the key pair was created.
        self.gmt_created = gmt_created
        # The ID of the key pair.
        self.key_pair_id = key_pair_id
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The private key of the key pair. The PEM-encoded private key that is in PKCS#8 format and adheres to the ADB connection specification.
        self.private_key_body = private_key_body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.private_key_body is not None:
            result['PrivateKeyBody'] = self.private_key_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PrivateKeyBody') is not None:
            self.private_key_body = m.get('PrivateKeyBody')
        return self


class CreateKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateKeyPairResponseBodyData = None,
        request_id: str = None,
    ):
        # The objects that are returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateKeyPairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKeyPairResponseBody = None,
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
            temp_model = CreateKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyGroupRequestNetRedirectPolicyRules(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        target: str = None,
    ):
        # The type of the rule.
        # 
        # Valid values:
        # 
        # *   prc: an application package name.
        # *   domain: a domain name.
        self.rule_type = rule_type
        # The name of the application package or domain name.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class CreatePolicyGroupRequestNetRedirectPolicy(TeaModel):
    def __init__(
        self,
        custom_proxy: str = None,
        host_addr: str = None,
        net_redirect: str = None,
        port: str = None,
        proxy_password: str = None,
        proxy_type: str = None,
        proxy_user_name: str = None,
        rules: List[CreatePolicyGroupRequestNetRedirectPolicyRules] = None,
    ):
        # Specifies whether to manually configure a custom proxy.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.custom_proxy = custom_proxy
        # The IPv4 address of the custom proxy.
        self.host_addr = host_addr
        # Specifies whether to enable the network redirection feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.net_redirect = net_redirect
        # The port of the custom proxy. Valid values: 1 to 65535.
        self.port = port
        # The password of the proxy. The password must be 1 to 256 in length and cannot contain Chinese character or space characters.
        self.proxy_password = proxy_password
        # The type of the proxy protocol.
        # 
        # Valid values:
        # 
        # *   socks5.
        self.proxy_type = proxy_type
        # The username of the proxy. The name must be 1 to 256 in length and cannot contain Chinese character or space characters.
        self.proxy_user_name = proxy_user_name
        # The proxy rules. You can create up to 100 proxy rules.
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
        if self.custom_proxy is not None:
            result['CustomProxy'] = self.custom_proxy
        if self.host_addr is not None:
            result['HostAddr'] = self.host_addr
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_user_name is not None:
            result['ProxyUserName'] = self.proxy_user_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomProxy') is not None:
            self.custom_proxy = m.get('CustomProxy')
        if m.get('HostAddr') is not None:
            self.host_addr = m.get('HostAddr')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('ProxyUserName') is not None:
            self.proxy_user_name = m.get('ProxyUserName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = CreatePolicyGroupRequestNetRedirectPolicyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class CreatePolicyGroupRequestWatermark(TeaModel):
    def __init__(
        self,
        watermark_color: int = None,
        watermark_custom_text: str = None,
        watermark_font_size: int = None,
        watermark_switch: str = None,
        watermark_transparency_value: int = None,
        watermark_types: List[str] = None,
    ):
        self.watermark_color = watermark_color
        self.watermark_custom_text = watermark_custom_text
        self.watermark_font_size = watermark_font_size
        self.watermark_switch = watermark_switch
        self.watermark_transparency_value = watermark_transparency_value
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_color is not None:
            result['WatermarkColor'] = self.watermark_color
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_font_size is not None:
            result['WatermarkFontSize'] = self.watermark_font_size
        if self.watermark_switch is not None:
            result['WatermarkSwitch'] = self.watermark_switch
        if self.watermark_transparency_value is not None:
            result['WatermarkTransparencyValue'] = self.watermark_transparency_value
        if self.watermark_types is not None:
            result['WatermarkTypes'] = self.watermark_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkColor') is not None:
            self.watermark_color = m.get('WatermarkColor')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkFontSize') is not None:
            self.watermark_font_size = m.get('WatermarkFontSize')
        if m.get('WatermarkSwitch') is not None:
            self.watermark_switch = m.get('WatermarkSwitch')
        if m.get('WatermarkTransparencyValue') is not None:
            self.watermark_transparency_value = m.get('WatermarkTransparencyValue')
        if m.get('WatermarkTypes') is not None:
            self.watermark_types = m.get('WatermarkTypes')
        return self


class CreatePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy: CreatePolicyGroupRequestNetRedirectPolicy = None,
        policy_group_name: str = None,
        policy_type: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        watermark: CreatePolicyGroupRequestWatermark = None,
    ):
        # Specifies whether to enable the webcam redirection feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.camera_redirect = camera_redirect
        # The read/write permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: read and write.
        # *   off: read/write disabled.
        self.clipboard = clipboard
        # The file transfer policy of the Alibaba Cloud Workspace web client.
        # 
        # Valid values:
        # 
        # *   all: File upload and download are supported.
        # *   download: Only file download is supported.
        # *   upload: Only file upload is supported.
        # *   off: File upload or download is forbidden.
        self.html_5file_transfer = html_5file_transfer
        # The read/write permissions on the on-premises drive.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.local_drive = local_drive
        # Specifies whether to lock the resolution.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.lock_resolution = lock_resolution
        # The network redirection policy.
        self.net_redirect_policy = net_redirect_policy
        # The name of the policy.
        self.policy_group_name = policy_group_name
        self.policy_type = policy_type
        # The height of the resolution. Unit: pixels.
        self.resolution_height = resolution_height
        # The width of the resolution. Unit: pixels.
        self.resolution_width = resolution_width
        self.watermark = watermark

    def validate(self):
        if self.net_redirect_policy:
            self.net_redirect_policy.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy.to_map()
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            temp_model = CreatePolicyGroupRequestNetRedirectPolicy()
            self.net_redirect_policy = temp_model.from_map(m['NetRedirectPolicy'])
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('Watermark') is not None:
            temp_model = CreatePolicyGroupRequestWatermark()
            self.watermark = temp_model.from_map(m['Watermark'])
        return self


class CreatePolicyGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy_shrink: str = None,
        policy_group_name: str = None,
        policy_type: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        watermark_shrink: str = None,
    ):
        # Specifies whether to enable the webcam redirection feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.camera_redirect = camera_redirect
        # The read/write permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: read and write.
        # *   off: read/write disabled.
        self.clipboard = clipboard
        # The file transfer policy of the Alibaba Cloud Workspace web client.
        # 
        # Valid values:
        # 
        # *   all: File upload and download are supported.
        # *   download: Only file download is supported.
        # *   upload: Only file upload is supported.
        # *   off: File upload or download is forbidden.
        self.html_5file_transfer = html_5file_transfer
        # The read/write permissions on the on-premises drive.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.local_drive = local_drive
        # Specifies whether to lock the resolution.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.lock_resolution = lock_resolution
        # The network redirection policy.
        self.net_redirect_policy_shrink = net_redirect_policy_shrink
        # The name of the policy.
        self.policy_group_name = policy_group_name
        self.policy_type = policy_type
        # The height of the resolution. Unit: pixels.
        self.resolution_height = resolution_height
        # The width of the resolution. Unit: pixels.
        self.resolution_width = resolution_width
        self.watermark_shrink = watermark_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy_shrink is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy_shrink
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.watermark_shrink is not None:
            result['Watermark'] = self.watermark_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            self.net_redirect_policy_shrink = m.get('NetRedirectPolicy')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('Watermark') is not None:
            self.watermark_shrink = m.get('Watermark')
        return self


class CreatePolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        policy_group_id: str = None,
        request_id: str = None,
    ):
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyGroupResponseBody = None,
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
            temp_model = CreatePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScreenshotRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        oss_bucket_name: str = None,
        skip_check_policy_config: str = None,
    ):
        # The IDs of the cloud phone instances. You can create multiple snapshots simultaneously.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # The name of the OSS bucket. The name must start with "cloudphone-saved-bucket-". The OSS bucket and the cloud phone instance must be in the same region. If you leave this parameter empty, the system will create a default OSS bucket named “cloudphone-saved-bucket-{Region of the cloud phone instance}-{AliUid}.”
        self.oss_bucket_name = oss_bucket_name
        # Specifies whether to bypass the snapshot policy control. Default value: false.
        self.skip_check_policy_config = skip_check_policy_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.skip_check_policy_config is not None:
            result['SkipCheckPolicyConfig'] = self.skip_check_policy_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('SkipCheckPolicyConfig') is not None:
            self.skip_check_policy_config = m.get('SkipCheckPolicyConfig')
        return self


class CreateScreenshotResponseBodyTasks(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        task_id: str = None,
    ):
        # The ID of the cloud phone instance.
        self.android_instance_id = android_instance_id
        # The ID of the task. You can use the task ID with the DescribeTasks operation to get the download link for the screenshot.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateScreenshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[CreateScreenshotResponseBodyTasks] = None,
    ):
        # The ID of the request. If the request fails, share this ID with technical support to help diagnose the issue.
        self.request_id = request_id
        # The tasks.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = CreateScreenshotResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class CreateScreenshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScreenshotResponseBody = None,
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
            temp_model = CreateScreenshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        instance_group_ids: List[str] = None,
    ):
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        return self


class DeleteAndroidInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAndroidInstanceGroupResponseBody = None,
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
            temp_model = DeleteAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppsRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
    ):
        # The IDs of the applications.
        self.app_id_list = app_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        return self


class DeleteAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppsResponseBody = None,
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
            temp_model = DeleteAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCloudPhoneNodesRequest(TeaModel):
    def __init__(
        self,
        node_ids: List[str] = None,
    ):
        # The cloud phone matrix IDs.
        self.node_ids = node_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        return self


class DeleteCloudPhoneNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCloudPhoneNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCloudPhoneNodesResponseBody = None,
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
            temp_model = DeleteCloudPhoneNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImagesRequest(TeaModel):
    def __init__(
        self,
        image_ids: List[str] = None,
    ):
        # The IDs of the images.
        # 
        # This parameter is required.
        self.image_ids = image_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        return self


class DeleteImagesShrinkRequest(TeaModel):
    def __init__(
        self,
        image_ids_shrink: str = None,
    ):
        # The IDs of the images.
        # 
        # This parameter is required.
        self.image_ids_shrink = image_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids_shrink is not None:
            result['ImageIds'] = self.image_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids_shrink = m.get('ImageIds')
        return self


class DeleteImagesResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_delete_image_ids: List[str] = None,
        success_delete_image_ids: List[str] = None,
    ):
        # The IDs of the images that failed to be deleted.
        self.fail_delete_image_ids = fail_delete_image_ids
        # The IDs of the images that are successfully deleted.
        self.success_delete_image_ids = success_delete_image_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_delete_image_ids is not None:
            result['FailDeleteImageIds'] = self.fail_delete_image_ids
        if self.success_delete_image_ids is not None:
            result['SuccessDeleteImageIds'] = self.success_delete_image_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailDeleteImageIds') is not None:
            self.fail_delete_image_ids = m.get('FailDeleteImageIds')
        if m.get('SuccessDeleteImageIds') is not None:
            self.success_delete_image_ids = m.get('SuccessDeleteImageIds')
        return self


class DeleteImagesResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteImagesResponseBodyData = None,
        request_id: str = None,
    ):
        # The images.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteImagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImagesResponseBody = None,
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
            temp_model = DeleteImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyPairsRequest(TeaModel):
    def __init__(
        self,
        key_pair_ids: List[str] = None,
    ):
        # The IDs of the ADB key pairs.
        self.key_pair_ids = key_pair_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_ids is not None:
            result['KeyPairIds'] = self.key_pair_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairIds') is not None:
            self.key_pair_ids = m.get('KeyPairIds')
        return self


class DeleteKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKeyPairsResponseBody = None,
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
            temp_model = DeleteKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        policy_group_ids: List[str] = None,
    ):
        # The IDs of the policies.
        # 
        # This parameter is required.
        self.policy_group_ids = policy_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')
        return self


class DeletePolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyGroupResponseBody = None,
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
            temp_model = DeletePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAndroidInstanceGroupsRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        charge_type: str = None,
        instance_group_ids: List[str] = None,
        instance_group_name: str = None,
        key_pair_id: str = None,
        max_results: int = None,
        next_token: str = None,
        policy_group_id: str = None,
        sale_mode: str = None,
        status: str = None,
    ):
        # The ID of the region.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        self.charge_type = charge_type
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The name of the instance group. Instance groups support fuzzy search by name.
        self.instance_group_name = instance_group_name
        # The ID of the key pair.
        self.key_pair_id = key_pair_id
        # The maximum number of entries per page. Value range: 0 to 100. Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The purchase mode of cloud phone instances.
        # 
        # Valid values:
        # 
        # *   Instance (default): the instance group mode.
        # *   Node: the matrix mode [whitelisted].
        self.sale_mode = sale_mode
        # The status of the instance group.
        # 
        # Valid values:
        # 
        # *   UPDATING_FAILED: The image update for the instance group failed.
        # *   FAILED: The instance group failed to be created.
        # *   RUNNING: The instance group is available.
        # *   EXPIRED: The instance group expired.
        # *   DELETING: The instance group is being deleted.
        # *   DELETED: The instance group is deleted.
        # *   UPDATING: The instance group is undergoing an image update.
        # *   CREATING: The instance group is being created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        disk_type: str = None,
    ):
        # The size of the disk. Unit: GB.
        self.disk_size = disk_size
        # The type of the disk.
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        architecture_type: str = None,
        available_instance_amount: int = None,
        charge_type: str = None,
        cpu: str = None,
        disks: List[DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks] = None,
        enable_ipv_6: bool = None,
        error_code: str = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        installed_app_list: str = None,
        instance_group_id: str = None,
        instance_group_name: str = None,
        instance_group_spec: str = None,
        instance_group_spec_describe: str = None,
        instance_group_status: str = None,
        ipv_6bandwidth: int = None,
        memory: int = None,
        number_of_instances: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        region_id: str = None,
        rendering_type: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        sale_mode: str = None,
        system_version: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The type of the architecture.
        self.architecture_type = architecture_type
        # The number of available instances.
        # 
        # >  Available instances are those not in the Deleting or Deleted state.
        self.available_instance_amount = available_instance_amount
        # The billing method.
        self.charge_type = charge_type
        # The number of vCPUs.
        self.cpu = cpu
        # The disks.
        self.disks = disks
        self.enable_ipv_6 = enable_ipv_6
        # The cause of the creation failure.
        self.error_code = error_code
        # The time when the instance group was created.
        self.gmt_create = gmt_create
        # The time when the subscription instance group expires.
        self.gmt_expired = gmt_expired
        # The time when the instance group was updated.
        self.gmt_modified = gmt_modified
        # The ID of the image.
        self.image_id = image_id
        # The list of installed applications.
        self.installed_app_list = installed_app_list
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The name of the instance group.
        self.instance_group_name = instance_group_name
        # The specifications of the instance group.
        self.instance_group_spec = instance_group_spec
        # The description of the instance group specifications.
        self.instance_group_spec_describe = instance_group_spec_describe
        # The status of the instance group.
        self.instance_group_status = instance_group_status
        self.ipv_6bandwidth = ipv_6bandwidth
        # The memory size.
        self.memory = memory
        # The number of instances in the instance group.
        self.number_of_instances = number_of_instances
        # The ID of the network.
        self.office_site_id = office_site_id
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The ID of the region.
        self.region_id = region_id
        # The rendering mode of the instance group.
        # 
        # Valid values:
        # 
        # *   GPURemote: GPU remote rendering.
        # *   CPU: CPU rendering.
        # *   GPUocal: GPU local rendering.
        self.rendering_type = rendering_type
        # The height of the resolution.
        self.resolution_height = resolution_height
        # The width of the resolution.
        self.resolution_width = resolution_width
        # The sales mode.
        self.sale_mode = sale_mode
        # The version of the operating system.
        self.system_version = system_version
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.available_instance_amount is not None:
            result['AvailableInstanceAmount'] = self.available_instance_amount
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.installed_app_list is not None:
            result['InstalledAppList'] = self.installed_app_list
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name
        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec
        if self.instance_group_spec_describe is not None:
            result['InstanceGroupSpecDescribe'] = self.instance_group_spec_describe
        if self.instance_group_status is not None:
            result['InstanceGroupStatus'] = self.instance_group_status
        if self.ipv_6bandwidth is not None:
            result['Ipv6Bandwidth'] = self.ipv_6bandwidth
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.number_of_instances is not None:
            result['NumberOfInstances'] = self.number_of_instances
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('AvailableInstanceAmount') is not None:
            self.available_instance_amount = m.get('AvailableInstanceAmount')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstalledAppList') is not None:
            self.installed_app_list = m.get('InstalledAppList')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')
        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')
        if m.get('InstanceGroupSpecDescribe') is not None:
            self.instance_group_spec_describe = m.get('InstanceGroupSpecDescribe')
        if m.get('InstanceGroupStatus') is not None:
            self.instance_group_status = m.get('InstanceGroupStatus')
        if m.get('Ipv6Bandwidth') is not None:
            self.ipv_6bandwidth = m.get('Ipv6Bandwidth')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NumberOfInstances') is not None:
            self.number_of_instances = m.get('NumberOfInstances')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeAndroidInstanceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        instance_group_model: List[DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The instance group.
        self.instance_group_model = instance_group_model
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_group_model:
            for k in self.instance_group_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceGroupModel'] = []
        if self.instance_group_model is not None:
            for k in self.instance_group_model:
                result['InstanceGroupModel'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_group_model = []
        if m.get('InstanceGroupModel') is not None:
            for k in m.get('InstanceGroupModel'):
                temp_model = DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel()
                self.instance_group_model.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAndroidInstanceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAndroidInstanceGroupsResponseBody = None,
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
            temp_model = DescribeAndroidInstanceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAndroidInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class DescribeAndroidInstancesRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        android_instance_name: str = None,
        app_manage_policy_id: str = None,
        authorized_user_id: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        instance_group_id: str = None,
        instance_group_ids: List[str] = None,
        instance_group_name: str = None,
        key_pair_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_id: str = None,
        node_name: str = None,
        office_site_ids: List[str] = None,
        qos_rule_ids: List[str] = None,
        sale_mode: str = None,
        status: str = None,
        tag: List[DescribeAndroidInstancesRequestTag] = None,
    ):
        # The IDs of the instances.
        self.android_instance_ids = android_instance_ids
        # The name of the instance.
        self.android_instance_name = android_instance_name
        self.app_manage_policy_id = app_manage_policy_id
        self.authorized_user_id = authorized_user_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/2807298.html) operation to query the regions where Cloud Phone is supported.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        self.charge_type = charge_type
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The name of the instance group.
        self.instance_group_name = instance_group_name
        # The ID of the bound key pair.
        self.key_pair_id = key_pair_id
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        self.office_site_ids = office_site_ids
        self.qos_rule_ids = qos_rule_ids
        # The sales mode.
        # 
        # Valid values:
        # 
        # *   Instance: the standard mode.
        # *   Node: the node mode.
        self.sale_mode = sale_mode
        # The state of the instance.
        # 
        # Valid values:
        # 
        # *   BACKUPING: The instance is being backed up.
        # *   STARTING: The instance is being started.
        # *   RUNNING: The instance group is available.
        # *   DELETING: The instance is being deleted.
        # *   BACKUP_FAILED: The backup operation failed.
        # *   DELETED: The instance is deleted.
        # *   FAILED: The instance failed to be created.
        # *   STOPPED: The instance is stopped.
        # *   RECOVERING: The instance has an ongoing file recovery task.
        # *   UNAVAILABLE: The instance has an exception.
        # *   REBOOTING: The instance is being restarted.
        # *   RESETTING: The instance is being reset.
        # *   STOPPING: The instance is being stopped.
        # *   RECOVER_FAILED: The file recovery task failed.
        # *   CREATING: The instance is being created.
        self.status = status
        # The tags of the resources.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name
        if self.app_manage_policy_id is not None:
            result['AppManagePolicyId'] = self.app_manage_policy_id
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.office_site_ids is not None:
            result['OfficeSiteIds'] = self.office_site_ids
        if self.qos_rule_ids is not None:
            result['QosRuleIds'] = self.qos_rule_ids
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')
        if m.get('AppManagePolicyId') is not None:
            self.app_manage_policy_id = m.get('AppManagePolicyId')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OfficeSiteIds') is not None:
            self.office_site_ids = m.get('OfficeSiteIds')
        if m.get('QosRuleIds') is not None:
            self.qos_rule_ids = m.get('QosRuleIds')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeAndroidInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeAndroidInstancesResponseBodyInstanceModelAppManagePolicy(TeaModel):
    def __init__(
        self,
        app_manage_policy_id: str = None,
        app_manage_policy_name: str = None,
    ):
        self.app_manage_policy_id = app_manage_policy_id
        self.app_manage_policy_name = app_manage_policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_manage_policy_id is not None:
            result['AppManagePolicyId'] = self.app_manage_policy_id
        if self.app_manage_policy_name is not None:
            result['AppManagePolicyName'] = self.app_manage_policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppManagePolicyId') is not None:
            self.app_manage_policy_id = m.get('AppManagePolicyId')
        if m.get('AppManagePolicyName') is not None:
            self.app_manage_policy_name = m.get('AppManagePolicyName')
        return self


class DescribeAndroidInstancesResponseBodyInstanceModelDisks(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        disk_type: str = None,
    ):
        # The disk size. Unit: GB.
        self.disk_size = disk_size
        # The type of the disk.
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeAndroidInstancesResponseBodyInstanceModelDisplayConfig(TeaModel):
    def __init__(
        self,
        dpi: int = None,
        fps: int = None,
        lock_resolution: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.dpi = dpi
        self.fps = fps
        self.lock_resolution = lock_resolution
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dpi is not None:
            result['Dpi'] = self.dpi
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dpi') is not None:
            self.dpi = m.get('Dpi')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        return self


class DescribeAndroidInstancesResponseBodyInstanceModelTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class DescribeAndroidInstancesResponseBodyInstanceModel(TeaModel):
    def __init__(
        self,
        android_instance_group_id: str = None,
        android_instance_group_name: str = None,
        android_instance_id: str = None,
        android_instance_name: str = None,
        android_instance_status: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_manage_policy: DescribeAndroidInstancesResponseBodyInstanceModelAppManagePolicy = None,
        authorized_user_id: str = None,
        bind_user_id: str = None,
        charge_type: str = None,
        cpu: str = None,
        disks: List[DescribeAndroidInstancesResponseBodyInstanceModelDisks] = None,
        display_config: DescribeAndroidInstancesResponseBodyInstanceModelDisplayConfig = None,
        error_code: str = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        image_version: str = None,
        instance_type: str = None,
        key_pair_id: str = None,
        memory: int = None,
        network_interface_ip: str = None,
        network_interface_ipv_6address: str = None,
        office_site_id: str = None,
        persistent_app_instance_id: str = None,
        policy_group_id: str = None,
        public_ip_address: str = None,
        public_ipv_6address: str = None,
        qos_rule_id: str = None,
        rate: int = None,
        region_id: str = None,
        rendering_type: str = None,
        session_status: str = None,
        tags: List[DescribeAndroidInstancesResponseBodyInstanceModelTags] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the instance group.
        self.android_instance_group_id = android_instance_group_id
        # The name of the instance group.
        self.android_instance_group_name = android_instance_group_name
        # The ID of the instance.
        self.android_instance_id = android_instance_id
        # The name of the instance.
        self.android_instance_name = android_instance_name
        # The state of the instance.
        self.android_instance_status = android_instance_status
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the physical instance.
        self.app_instance_id = app_instance_id
        self.app_manage_policy = app_manage_policy
        # The ID of the user to whom the instance is assigned.
        self.authorized_user_id = authorized_user_id
        # The ID of the bound user.
        self.bind_user_id = bind_user_id
        # The billing method of the instance.
        self.charge_type = charge_type
        # The number of vCPUs.
        self.cpu = cpu
        # The disks.
        self.disks = disks
        self.display_config = display_config
        # The cause of the instance data backup failure or restoration failure.
        self.error_code = error_code
        # The time when the instance was created.
        self.gmt_create = gmt_create
        # The time when the subscription instance group expires.
        self.gmt_expired = gmt_expired
        # The time when the instance was modified.
        self.gmt_modified = gmt_modified
        self.image_id = image_id
        # The version of the image.
        self.image_version = image_version
        # The type of the instance.
        self.instance_type = instance_type
        # The ID of the key pair.
        self.key_pair_id = key_pair_id
        # The memory size.
        self.memory = memory
        # The IP address of the ENI.
        self.network_interface_ip = network_interface_ip
        # >  This parameter is not publicly available.
        self.network_interface_ipv_6address = network_interface_ipv_6address
        # The office network ID.
        self.office_site_id = office_site_id
        # The ID of the persistent session.
        self.persistent_app_instance_id = persistent_app_instance_id
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The public IP address.
        self.public_ip_address = public_ip_address
        # >  This parameter is not publicly available.
        self.public_ipv_6address = public_ipv_6address
        self.qos_rule_id = qos_rule_id
        # The progress of instance data backup or restoration.
        self.rate = rate
        # The region ID of the instance.
        self.region_id = region_id
        # The rendering type.
        self.rendering_type = rendering_type
        # The session status.
        # 
        # Valid values:
        # 
        # *   disConnect: The session is disconnected.
        # *   connect: The session is connected.
        self.session_status = session_status
        # The tags.
        self.tags = tags
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.app_manage_policy:
            self.app_manage_policy.validate()
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.display_config:
            self.display_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_group_id is not None:
            result['AndroidInstanceGroupId'] = self.android_instance_group_id
        if self.android_instance_group_name is not None:
            result['AndroidInstanceGroupName'] = self.android_instance_group_name
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name
        if self.android_instance_status is not None:
            result['AndroidInstanceStatus'] = self.android_instance_status
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_manage_policy is not None:
            result['AppManagePolicy'] = self.app_manage_policy.to_map()
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.bind_user_id is not None:
            result['BindUserId'] = self.bind_user_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.display_config is not None:
            result['DisplayConfig'] = self.display_config.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.network_interface_ipv_6address is not None:
            result['NetworkInterfaceIpv6Address'] = self.network_interface_ipv_6address
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.persistent_app_instance_id is not None:
            result['PersistentAppInstanceId'] = self.persistent_app_instance_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.public_ipv_6address is not None:
            result['PublicIpv6Address'] = self.public_ipv_6address
        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceGroupId') is not None:
            self.android_instance_group_id = m.get('AndroidInstanceGroupId')
        if m.get('AndroidInstanceGroupName') is not None:
            self.android_instance_group_name = m.get('AndroidInstanceGroupName')
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')
        if m.get('AndroidInstanceStatus') is not None:
            self.android_instance_status = m.get('AndroidInstanceStatus')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppManagePolicy') is not None:
            temp_model = DescribeAndroidInstancesResponseBodyInstanceModelAppManagePolicy()
            self.app_manage_policy = temp_model.from_map(m['AppManagePolicy'])
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('BindUserId') is not None:
            self.bind_user_id = m.get('BindUserId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeAndroidInstancesResponseBodyInstanceModelDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('DisplayConfig') is not None:
            temp_model = DescribeAndroidInstancesResponseBodyInstanceModelDisplayConfig()
            self.display_config = temp_model.from_map(m['DisplayConfig'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('NetworkInterfaceIpv6Address') is not None:
            self.network_interface_ipv_6address = m.get('NetworkInterfaceIpv6Address')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PersistentAppInstanceId') is not None:
            self.persistent_app_instance_id = m.get('PersistentAppInstanceId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('PublicIpv6Address') is not None:
            self.public_ipv_6address = m.get('PublicIpv6Address')
        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeAndroidInstancesResponseBodyInstanceModelTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAndroidInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_model: List[DescribeAndroidInstancesResponseBodyInstanceModel] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The cloud phone instances.
        self.instance_model = instance_model
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_model:
            for k in self.instance_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceModel'] = []
        if self.instance_model is not None:
            for k in self.instance_model:
                result['InstanceModel'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_model = []
        if m.get('InstanceModel') is not None:
            for k in m.get('InstanceModel'):
                temp_model = DescribeAndroidInstancesResponseBodyInstanceModel()
                self.instance_model.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAndroidInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAndroidInstancesResponseBody = None,
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
            temp_model = DescribeAndroidInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        app_name: str = None,
        app_type: str = None,
        biz_region_id: str = None,
        installation_status: str = None,
        md5: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        # The IDs of the applications.
        self.app_id_list = app_id_list
        # The name of the application.
        self.app_name = app_name
        self.app_type = app_type
        # Region id.
        self.biz_region_id = biz_region_id
        # The installation/uninstallation status of the application.
        # 
        # Valid values:
        # 
        # *   INSTALLFAILED: The application failed to be installed.
        # *   UNINSTALLING: The application is being uninstalled.
        # *   INSTALLING: The application is being installed.
        # *   UNINSTALLED: The application is uninstalled.
        # *   INSTALLED: The application is installed.
        # *   UNINSTALLFAILED: The application failed to be uninstalled.
        self.installation_status = installation_status
        # The value of MD5.
        self.md5 = md5
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The status of the application.
        # 
        # Valid values:
        # 
        # *   FAILED: The application failed to be created.
        # *   NORMAL: The application is available.
        # *   CREATING: The application is being created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.installation_status is not None:
            result['InstallationStatus'] = self.installation_status
        if self.md5 is not None:
            result['MD5'] = self.md5
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('InstallationStatus') is not None:
            self.installation_status = m.get('InstallationStatus')
        if m.get('MD5') is not None:
            self.md5 = m.get('MD5')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        android_app_version: str = None,
        apk_size: str = None,
        app_id: int = None,
        app_name: str = None,
        app_type: str = None,
        biz_region_id: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon_url: str = None,
        installation_status: str = None,
        instance_group_list: List[str] = None,
        md5: str = None,
        package_name: str = None,
        status: str = None,
    ):
        # The version of the application.
        self.android_app_version = android_app_version
        # Apk size.
        self.apk_size = apk_size
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        self.app_type = app_type
        # Region id.
        self.biz_region_id = biz_region_id
        # The description of the application.
        self.description = description
        # The time when the application was created.
        self.gmt_create = gmt_create
        # The time when the application was last modified.
        self.gmt_modified = gmt_modified
        # The icon URL of the application.
        self.icon_url = icon_url
        # The installation/uninstallation status of the application.
        # 
        # Valid values:
        # 
        # *   INSTALLFAILED: The application failed to be installed.
        # *   UNINSTALLING: The application is being uninstalled.
        # *   INSTALLING: The application is being installed.
        # *   UNINSTALLED: The application is uninstalled.
        # *   INSTALLED: The application is installed.
        # *   UNINSTALLFAILED: The application failed to be uninstalled.
        self.installation_status = installation_status
        # The list of instance groups where the application is installed.
        self.instance_group_list = instance_group_list
        # The value of MD5.
        self.md5 = md5
        # The name of the application package.
        self.package_name = package_name
        # The status of the application.
        # 
        # Valid values:
        # 
        # *   FAILED: The application failed to be created.
        # *   NORMAL: The application is available.
        # *   CREATING: The application is being created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_app_version is not None:
            result['AndroidAppVersion'] = self.android_app_version
        if self.apk_size is not None:
            result['ApkSize'] = self.apk_size
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.installation_status is not None:
            result['InstallationStatus'] = self.installation_status
        if self.instance_group_list is not None:
            result['InstanceGroupList'] = self.instance_group_list
        if self.md5 is not None:
            result['MD5'] = self.md5
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidAppVersion') is not None:
            self.android_app_version = m.get('AndroidAppVersion')
        if m.get('ApkSize') is not None:
            self.apk_size = m.get('ApkSize')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('InstallationStatus') is not None:
            self.installation_status = m.get('InstallationStatus')
        if m.get('InstanceGroupList') is not None:
            self.instance_group_list = m.get('InstanceGroupList')
        if m.get('MD5') is not None:
            self.md5 = m.get('MD5')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeAppsResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The objects that are returned.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAppsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppsResponseBody = None,
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
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupFilesRequest(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        android_instance_name: str = None,
        backup_all: bool = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        description: str = None,
        end_time: str = None,
        end_user_id: str = None,
        instance_group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        start_time: str = None,
        status_list: List[str] = None,
    ):
        # The ID of the instance.
        self.android_instance_id = android_instance_id
        # The name of the instance. Fuzzy match is supported.
        self.android_instance_name = android_instance_name
        # Specifies whether the whole instance is backed up.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.backup_all = backup_all
        # The ID of the backup file.
        self.backup_file_id = backup_file_id
        # The name of the backup file. Fuzzy match is supported.
        self.backup_file_name = backup_file_name
        # The description of the backup file. Fuzzy match is supported.
        self.description = description
        # The end of the period for querying generated backup files.
        self.end_time = end_time
        # The owner of the backup file.
        self.end_user_id = end_user_id
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The beginning of the period for querying generated backup files.
        self.start_time = start_time
        # The status of the backup files.
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name
        if self.backup_all is not None:
            result['BackupAll'] = self.backup_all
        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id
        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')
        if m.get('BackupAll') is not None:
            self.backup_all = m.get('BackupAll')
        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')
        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class DescribeBackupFilesResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        android_instance_name: str = None,
        backup_all: bool = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        backup_file_path: str = None,
        description: str = None,
        end_user_id: str = None,
        file_size: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        instance_group_id: str = None,
        region_id: str = None,
        source_app_info_list: List[str] = None,
        source_file_path_list: List[str] = None,
        status: str = None,
        task_id: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # The ID of the instance.
        self.android_instance_id = android_instance_id
        # The name of the instance.
        self.android_instance_name = android_instance_name
        # Indicates whether the whole instance is backed up.
        self.backup_all = backup_all
        # The ID of the backup file.
        self.backup_file_id = backup_file_id
        # The name of the backup file.
        self.backup_file_name = backup_file_name
        # The directory in which the backup file is stored.
        self.backup_file_path = backup_file_path
        # The description of the backup file.
        self.description = description
        # The owner of the backup file.
        self.end_user_id = end_user_id
        # The total size of the source files.
        self.file_size = file_size
        # The time when the backup file was created.
        self.gmt_created = gmt_created
        # The time when the backup file was last updated.
        self.gmt_modified = gmt_modified
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The region ID.
        self.region_id = region_id
        # The names of the application packages that are backed up.
        self.source_app_info_list = source_app_info_list
        # The directories of the source files.
        self.source_file_path_list = source_file_path_list
        # The status of the backup file.
        # 
        # Valid values:
        # 
        # *   AVAILABLE
        # *   RECOVERING
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The endpoint of the OSS bucket that stores the backup file.
        self.upload_endpoint = upload_endpoint
        # The type of the backup.
        # 
        # Valid values:
        # 
        # *   OSS: backup files are stored in OSS buckets. .
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name
        if self.backup_all is not None:
            result['BackupAll'] = self.backup_all
        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id
        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name
        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path
        if self.description is not None:
            result['Description'] = self.description
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_app_info_list is not None:
            result['SourceAppInfoList'] = self.source_app_info_list
        if self.source_file_path_list is not None:
            result['SourceFilePathList'] = self.source_file_path_list
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')
        if m.get('BackupAll') is not None:
            self.backup_all = m.get('BackupAll')
        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')
        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')
        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceAppInfoList') is not None:
            self.source_app_info_list = m.get('SourceAppInfoList')
        if m.get('SourceFilePathList') is not None:
            self.source_file_path_list = m.get('SourceFilePathList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class DescribeBackupFilesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeBackupFilesResponseBodyData] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The backup files that are returned.
        self.data = data
        # The total number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request. If the request fails, provide this ID to technical support to assist in diagnosing the issue.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeBackupFilesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupFilesResponseBody = None,
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
            temp_model = DescribeBackupFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudPhoneNodesRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        charge_type: str = None,
        max_results: str = None,
        next_token: str = None,
        node_ids: List[str] = None,
        node_name: str = None,
        server_type: str = None,
        status: str = None,
    ):
        # The region ID.
        self.biz_region_id = biz_region_id
        # The billing method. Only the subscription billing method is supported.
        self.charge_type = charge_type
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If a query doesn\\"t return all results, the response includes a NextToken value for pagination. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The matrix IDs.
        self.node_ids = node_ids
        # The matrix name.
        self.node_name = node_name
        # The matrix specification.
        # 
        # Valid values:
        # 
        # *   cpm.gn6.gx1
        self.server_type = server_type
        # The matrix status.
        # 
        # Valid values:
        # 
        # *   FAILED: The matrix failed to be created.
        # *   RUNNING: The matrix is available.
        # *   DELETING: The matrix is being deleted.
        # *   NODE_READY: The matrix is ready, and cloud phone instances are being created.
        # *   DELETED: The matrix is deleted.
        # *   CREATING: The matrix is being created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCloudPhoneNodesResponseBodyNodeModelNetworkInfos(TeaModel):
    def __init__(
        self,
        network_id: str = None,
        v_switch_id: str = None,
    ):
        self.network_id = network_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeCloudPhoneNodesResponseBodyNodeModel(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        cpu: str = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        instance_type: str = None,
        memory: int = None,
        network_id: str = None,
        network_infos: List[DescribeCloudPhoneNodesResponseBodyNodeModelNetworkInfos] = None,
        node_id: str = None,
        node_name: str = None,
        phone_count: int = None,
        region_id: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        server_type: str = None,
        share_data_volume: int = None,
        status: str = None,
        v_switch_id: str = None,
    ):
        # The billing method.
        self.charge_type = charge_type
        # The number of CPU cores.
        self.cpu = cpu
        # The creation time.
        self.gmt_create = gmt_create
        # The expiration time of the subscription matrix.
        self.gmt_expired = gmt_expired
        # The last modification time.
        self.gmt_modified = gmt_modified
        self.instance_type = instance_type
        # The memory size. Unit: GB.
        self.memory = memory
        # The network ID.
        self.network_id = network_id
        self.network_infos = network_infos
        # The matrix ID.
        self.node_id = node_id
        # The matrix name.
        self.node_name = node_name
        # The number of cloud phone instances per matrix.
        self.phone_count = phone_count
        # The region ID.
        self.region_id = region_id
        # The height of the resolution. Unit: pixel.
        self.resolution_height = resolution_height
        # The width of the resolution. Unit: pixel.
        self.resolution_width = resolution_width
        # The matrix specification.
        self.server_type = server_type
        # The size of the shared storage. Unit: GiB.
        self.share_data_volume = share_data_volume
        # The matrix status.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.network_infos:
            for k in self.network_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        result['NetworkInfos'] = []
        if self.network_infos is not None:
            for k in self.network_infos:
                result['NetworkInfos'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.share_data_volume is not None:
            result['ShareDataVolume'] = self.share_data_volume
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        self.network_infos = []
        if m.get('NetworkInfos') is not None:
            for k in m.get('NetworkInfos'):
                temp_model = DescribeCloudPhoneNodesResponseBodyNodeModelNetworkInfos()
                self.network_infos.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('ShareDataVolume') is not None:
            self.share_data_volume = m.get('ShareDataVolume')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeCloudPhoneNodesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_model: List[DescribeCloudPhoneNodesResponseBodyNodeModel] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   ****\
        self.next_token = next_token
        # The matrixes.
        self.node_model = node_model
        # The request ID.
        self.request_id = request_id
        # The total number of cloud phone instances.
        self.total_count = total_count

    def validate(self):
        if self.node_model:
            for k in self.node_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NodeModel'] = []
        if self.node_model is not None:
            for k in self.node_model:
                result['NodeModel'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.node_model = []
        if m.get('NodeModel') is not None:
            for k in m.get('NodeModel'):
                temp_model = DescribeCloudPhoneNodesResponseBodyNodeModel()
                self.node_model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudPhoneNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudPhoneNodesResponseBody = None,
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
            temp_model = DescribeCloudPhoneNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisplayConfigRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
    ):
        self.android_instance_ids = android_instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        return self


class DescribeDisplayConfigResponseBodyDisplayConfigModel(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        dpi: int = None,
        fps: int = None,
        lock_resolution: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.android_instance_id = android_instance_id
        self.dpi = dpi
        self.fps = fps
        self.lock_resolution = lock_resolution
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.dpi is not None:
            result['Dpi'] = self.dpi
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('Dpi') is not None:
            self.dpi = m.get('Dpi')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        return self


class DescribeDisplayConfigResponseBody(TeaModel):
    def __init__(
        self,
        display_config_model: List[DescribeDisplayConfigResponseBodyDisplayConfigModel] = None,
        request_id: str = None,
    ):
        self.display_config_model = display_config_model
        self.request_id = request_id

    def validate(self):
        if self.display_config_model:
            for k in self.display_config_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DisplayConfigModel'] = []
        if self.display_config_model is not None:
            for k in self.display_config_model:
                result['DisplayConfigModel'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.display_config_model = []
        if m.get('DisplayConfigModel') is not None:
            for k in m.get('DisplayConfigModel'):
                temp_model = DescribeDisplayConfigResponseBodyDisplayConfigModel()
                self.display_config_model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDisplayConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDisplayConfigResponseBody = None,
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
            temp_model = DescribeDisplayConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageListRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        image_package_type: str = None,
        image_type: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # Image package type.
        self.image_package_type = image_package_type
        # The type of the image.
        # 
        # Valid values:
        # 
        # *   User: custom images.
        # *   System: system images.
        # 
        # This parameter is required.
        self.image_type = image_type
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The state of the image.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The image is available.
        # *   DELETE: The image is deleted.
        # *   INIT: The image is being initialized.
        # *   CREATE_FAILED: The image failed to be created.
        # *   CREATING: The image is being created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_package_type is not None:
            result['ImagePackageType'] = self.image_package_type
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImagePackageType') is not None:
            self.image_package_type = m.get('ImagePackageType')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeImageListResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        image_name: str = None,
        image_region_distribute_map: Dict[str, DataImageRegionDistributeMapValue] = None,
        image_region_list: List[str] = None,
        image_type: str = None,
        image_version: str = None,
        language: str = None,
        release_time: str = None,
        rendering_type: str = None,
        status: str = None,
        system_type: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The description of the image.
        self.description = description
        # The time when the image was created.
        self.gmt_create = gmt_create
        # The time when the image was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The region where the image is distributed. The key is the region and the value is the distribution information.
        self.image_region_distribute_map = image_region_distribute_map
        # The list of regions.
        self.image_region_list = image_region_list
        # The type of the image.
        # 
        # Valid values:
        # 
        # *   User: custom images.
        # *   System: system images.
        self.image_type = image_type
        self.image_version = image_version
        # The language of the image.
        self.language = language
        # The time when the image was published.
        self.release_time = release_time
        # The rendering type.
        # 
        # Valid values:
        # 
        # *   GPURemote
        # *   CPU
        # *   GPULocal
        self.rendering_type = rendering_type
        # The state of the image.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The image is available.
        # *   DELETE: The image is deleted.
        # *   INIT: The image is being initialized.
        # *   CREATE_FAILED: The image failed to be created.
        # *   CREATING: The image is being created.
        self.status = status
        # The OS type of the image.
        self.system_type = system_type

    def validate(self):
        if self.image_region_distribute_map:
            for v in self.image_region_distribute_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        result['ImageRegionDistributeMap'] = {}
        if self.image_region_distribute_map is not None:
            for k, v in self.image_region_distribute_map.items():
                result['ImageRegionDistributeMap'][k] = v.to_map()
        if self.image_region_list is not None:
            result['ImageRegionList'] = self.image_region_list
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.language is not None:
            result['Language'] = self.language
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type
        if self.status is not None:
            result['Status'] = self.status
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        self.image_region_distribute_map = {}
        if m.get('ImageRegionDistributeMap') is not None:
            for k, v in m.get('ImageRegionDistributeMap').items():
                temp_model = DataImageRegionDistributeMapValue()
                self.image_region_distribute_map[k] = temp_model.from_map(v)
        if m.get('ImageRegionList') is not None:
            self.image_region_list = m.get('ImageRegionList')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        return self


class DescribeImageListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeImageListResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The images.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeImageListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageListResponseBody = None,
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
            temp_model = DescribeImageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationsRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        invocation_id: str = None,
    ):
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The ID of the execution. You can retrieve the output of a command once by using either the execution ID or the cloud phone instance ID.
        # 
        # This parameter is required.
        self.invocation_id = invocation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        return self


class DescribeInvocationsResponseBodyData(TeaModel):
    def __init__(
        self,
        finish_time: str = None,
        instance_id: str = None,
        invocation_id: str = None,
        invocation_status: str = None,
        output: str = None,
        start_time: str = None,
    ):
        # The end time of the command execution.
        self.finish_time = finish_time
        # The ID of the cloud phone instance on which the command is executed.
        self.instance_id = instance_id
        # The ID of the execution.
        self.invocation_id = invocation_id
        # The execution state of the command.
        # 
        # Valid values:
        # 
        # *   Failed: The execution of the command failed.
        # *   Timeout: The execution of the command timed out.
        # *   Running: The command is being executed.
        # *   Success: The execution of the command is successful.
        # *   Pending: The command is waiting to be executed.
        self.invocation_status = invocation_status
        # The output of the command execution.
        self.output = output
        # The start time of the command execution.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.output is not None:
            result['Output'] = self.output
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeInvocationsResponseBodyData] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The objects that are returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeInvocationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInvocationsResponseBody = None,
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
            temp_model = DescribeInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyPairsRequest(TeaModel):
    def __init__(
        self,
        key_pair_ids: List[str] = None,
        key_pair_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The IDs of the ADB key pairs.
        self.key_pair_ids = key_pair_ids
        # The name of the ADB key pair.
        self.key_pair_name = key_pair_name
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_ids is not None:
            result['KeyPairIds'] = self.key_pair_ids
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairIds') is not None:
            self.key_pair_ids = m.get('KeyPairIds')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeKeyPairsResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
    ):
        # The time when the ADB key pair was created.
        self.gmt_created = gmt_created
        # The ID of the ADB key pair.
        self.key_pair_id = key_pair_id
        # The name of the ADB key pair.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class DescribeKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeKeyPairsResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The objects that are returned.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeKeyPairsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKeyPairsResponseBody = None,
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
            temp_model = DescribeKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        sale_mode: str = None,
    ):
        # The display language of the console. Valid values:
        # 
        # *   cn: Simplified Chinese
        # *   en: English
        self.accept_language = accept_language
        # The sales mode.
        # 
        # Valid values:
        # 
        # *   Instance: the instance group mode. [Default]
        # *   Node: the matrix mode. [Whitelist required]
        self.sale_mode = sale_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        return self


class DescribeRegionsResponseBodyRegionModels(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The region name.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        region_models: List[DescribeRegionsResponseBodyRegionModels] = None,
        request_id: str = None,
    ):
        # Available regions.
        self.region_models = region_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.region_models:
            for k in self.region_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionModels'] = []
        if self.region_models is not None:
            for k in self.region_models:
                result['RegionModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_models = []
        if m.get('RegionModels') is not None:
            for k in m.get('RegionModels'):
                temp_model = DescribeRegionsResponseBodyRegionModels()
                self.region_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeSpecRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        matrix_spec: str = None,
        max_results: int = None,
        next_token: str = None,
        sale_mode: str = None,
        spec_ids: List[str] = None,
        spec_status: str = None,
        spec_type: str = None,
    ):
        self.biz_region_id = biz_region_id
        # The matrix specification.
        # 
        # Valid values:
        # 
        # *   cpm.gn6.gx1
        self.matrix_spec = matrix_spec
        # The maximum number of items to return per page in a paginated query. The value range is 1 to 100, with a default value of 100.
        self.max_results = max_results
        # Indicates the starting position for reading. If left empty, it starts from the beginning.
        self.next_token = next_token
        # The purchase mode of cloud mobile phones.
        # 
        # Valid values:
        # 
        # *   Instance (default): the instance group mode.
        # *   Node: the matrix mode [whitelisted].
        self.sale_mode = sale_mode
        # List of specification IDs.
        self.spec_ids = spec_ids
        # Specification status.
        self.spec_status = spec_status
        # Specification type.
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.matrix_spec is not None:
            result['MatrixSpec'] = self.matrix_spec
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.spec_ids is not None:
            result['SpecIds'] = self.spec_ids
        if self.spec_status is not None:
            result['SpecStatus'] = self.spec_status
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('MatrixSpec') is not None:
            self.matrix_spec = m.get('MatrixSpec')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('SpecIds') is not None:
            self.spec_ids = m.get('SpecIds')
        if m.get('SpecStatus') is not None:
            self.spec_status = m.get('SpecStatus')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        return self


class DescribeSpecResponseBodySpecInfoModel(TeaModel):
    def __init__(
        self,
        core: int = None,
        max_phone_count: str = None,
        memory: int = None,
        min_phone_count: str = None,
        phone_count: str = None,
        resolution: str = None,
        spec_id: str = None,
        spec_status: str = None,
        spec_type: str = None,
        system_disk_size: int = None,
    ):
        # Number of CPU cores.
        self.core = core
        # The maximum number of cloud phone instances.
        self.max_phone_count = max_phone_count
        # Memory size.
        self.memory = memory
        # The minimum number of cloud phone instances.
        self.min_phone_count = min_phone_count
        self.phone_count = phone_count
        self.resolution = resolution
        # Specification ID.
        self.spec_id = spec_id
        # Specification status.
        self.spec_status = spec_status
        # Specification type.
        self.spec_type = spec_type
        # System disk size, in GB.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core is not None:
            result['Core'] = self.core
        if self.max_phone_count is not None:
            result['MaxPhoneCount'] = self.max_phone_count
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.min_phone_count is not None:
            result['MinPhoneCount'] = self.min_phone_count
        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.spec_status is not None:
            result['SpecStatus'] = self.spec_status
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')
        if m.get('MaxPhoneCount') is not None:
            self.max_phone_count = m.get('MaxPhoneCount')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MinPhoneCount') is not None:
            self.min_phone_count = m.get('MinPhoneCount')
        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('SpecStatus') is not None:
            self.spec_status = m.get('SpecStatus')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeSpecResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        spec_info_model: List[DescribeSpecResponseBodySpecInfoModel] = None,
        total_count: int = None,
    ):
        # Indicates the current read position returned by this call. An empty value means that all data has been read.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # The specifications.
        self.spec_info_model = spec_info_model
        # Total number of items.
        self.total_count = total_count

    def validate(self):
        if self.spec_info_model:
            for k in self.spec_info_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpecInfoModel'] = []
        if self.spec_info_model is not None:
            for k in self.spec_info_model:
                result['SpecInfoModel'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spec_info_model = []
        if m.get('SpecInfoModel') is not None:
            for k in m.get('SpecInfoModel'):
                temp_model = DescribeSpecResponseBodySpecInfoModel()
                self.spec_info_model.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSpecResponseBody = None,
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
            temp_model = DescribeSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        invoke_id: str = None,
        level: int = None,
        max_results: int = None,
        next_token: str = None,
        param: str = None,
        parent_task_id: str = None,
        resource_ids: List[str] = None,
        task_ids: List[str] = None,
        task_status: str = None,
        task_statuses: List[str] = None,
        task_type: str = None,
        task_types: List[str] = None,
    ):
        # The ID of the cloud phone instance.
        self.instance_id = instance_id
        # The name of the cloud phone instance.
        self.instance_name = instance_name
        # The ID of the command execution. You can set the value to the last returned request ID.
        self.invoke_id = invoke_id
        # The level of the task. A value of 1 specifies a batch task. A value of 2 specifies an instance-level task.
        self.level = level
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The extension field.
        self.param = param
        # The ID of the parent task.
        self.parent_task_id = parent_task_id
        # The IDs of the resources.
        self.resource_ids = resource_ids
        # The IDs of the tasks.
        self.task_ids = task_ids
        # The state of the task.
        # 
        # Valid values:
        # 
        # *   PartFinished: The task is partially successful.
        # *   Finished: The task is completed.
        # *   Failed: The task failed.
        # *   Skipped: The task is skipped.
        # *   Processing: The task is running.
        # *   Waiting: The task is in queue.
        self.task_status = task_status
        # The status of the tasks.
        self.task_statuses = task_statuses
        # The type of the task.
        # 
        # Valid values:
        # 
        # *   BackupFile: backs up files.
        # *   StopInstance: stops cloud phone instances.
        # *   RebootInstance: restarts cloud phone instances.
        # *   StartApp: starts apps.
        # *   SendFile: uploads files.
        # *   RunCommand: sends remote command.
        # *   RestartApp: restarts apps.
        # *   ResetInstance: resets cloud phone instances.
        # *   RecoverFile: recovers files.
        # *   UninstallApp: uninstalls apps.
        # *   StopApp: stops apps.
        # *   Screenshot: takes screenshots.
        # *   InstallApp: installs apps.
        # *   FetchFile: downloads files.
        # *   UpdateGroupImage: replaces images.
        # *   StartInstance: starts instances.
        self.task_type = task_type
        # The types of the tasks.
        self.task_types = task_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.level is not None:
            result['Level'] = self.level
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.param is not None:
            result['Param'] = self.param
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_statuses is not None:
            result['TaskStatuses'] = self.task_statuses
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_types is not None:
            result['TaskTypes'] = self.task_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatuses') is not None:
            self.task_statuses = m.get('TaskStatuses')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')
        return self


class DescribeTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        failed_child_count: int = None,
        finish_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        invoke_id: str = None,
        level: int = None,
        operator: str = None,
        param: str = None,
        parent_task_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        result: str = None,
        running_child_count: int = None,
        start_time: str = None,
        success_child_count: int = None,
        task_id: str = None,
        task_status: str = None,
        task_type: str = None,
        total_child_count: int = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The total number of failed subtasks.
        self.failed_child_count = failed_child_count
        # The end time of the task.
        self.finish_time = finish_time
        # The ID of the cloud phone instance.
        self.instance_id = instance_id
        # The name of the cloud phone instance.
        self.instance_name = instance_name
        # The state of the cloud phone instance.
        self.instance_status = instance_status
        # The ID of the command execution.
        self.invoke_id = invoke_id
        # The level of the task.
        self.level = level
        # The operator.
        self.operator = operator
        # The parameters of the task.
        self.param = param
        # The ID of the parent task.
        self.parent_task_id = parent_task_id
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The execution result of the task.
        self.result = result
        # The total number of the subtasks that are running.
        self.running_child_count = running_child_count
        # The start time of the task.
        self.start_time = start_time
        # The total number of successfully executed subtasks.
        self.success_child_count = success_child_count
        # The ID of the task.
        self.task_id = task_id
        # The state of the task.
        self.task_status = task_status
        # The type of the task.
        self.task_type = task_type
        # The total number of subtasks of the current batch task.
        self.total_child_count = total_child_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.failed_child_count is not None:
            result['FailedChildCount'] = self.failed_child_count
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.level is not None:
            result['Level'] = self.level
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.param is not None:
            result['Param'] = self.param
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.result is not None:
            result['Result'] = self.result
        if self.running_child_count is not None:
            result['RunningChildCount'] = self.running_child_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.success_child_count is not None:
            result['SuccessChildCount'] = self.success_child_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.total_child_count is not None:
            result['TotalChildCount'] = self.total_child_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FailedChildCount') is not None:
            self.failed_child_count = m.get('FailedChildCount')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RunningChildCount') is not None:
            self.running_child_count = m.get('RunningChildCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SuccessChildCount') is not None:
            self.success_child_count = m.get('SuccessChildCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TotalChildCount') is not None:
            self.total_child_count = m.get('TotalChildCount')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeTasksResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The objects that are returned.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTasksResponseBody = None,
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
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachKeyPairRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        key_pair_id: str = None,
    ):
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        self.instance_ids = instance_ids
        # The ID of the ADB key pair.
        # 
        # This parameter is required.
        self.key_pair_id = key_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        return self


class DetachKeyPairResponseBodyData(TeaModel):
    def __init__(
        self,
        detached_instance_ids: List[str] = None,
        fail_count: int = None,
        key_pair_id: str = None,
        total_count: int = None,
    ):
        # The IDs of the cloud phone instances from which the ADB key pair is successfully detached.
        self.detached_instance_ids = detached_instance_ids
        # The number of the cloud phone instances from which the ADB key pair failed to be detached.
        self.fail_count = fail_count
        # The ID of the ADB key pair.
        self.key_pair_id = key_pair_id
        # The total number of the cloud phone instances.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detached_instance_ids is not None:
            result['DetachedInstanceIds'] = self.detached_instance_ids
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetachedInstanceIds') is not None:
            self.detached_instance_ids = m.get('DetachedInstanceIds')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DetachKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        data: DetachKeyPairResponseBodyData = None,
        request_id: str = None,
    ):
        # The object that is returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DetachKeyPairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachKeyPairResponseBody = None,
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
            temp_model = DetachKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisconnectAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
    ):
        # This parameter is required.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DisconnectAndroidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisconnectAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisconnectAndroidInstanceResponseBody = None,
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
            temp_model = DisconnectAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DistributeImageRequest(TeaModel):
    def __init__(
        self,
        distribute_region_list: List[str] = None,
        image_id: str = None,
    ):
        # The regions to which you want to distribute an image.
        # 
        # This parameter is required.
        self.distribute_region_list = distribute_region_list
        # The ID of the image that you want to distribute.
        # 
        # This parameter is required.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribute_region_list is not None:
            result['DistributeRegionList'] = self.distribute_region_list
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeRegionList') is not None:
            self.distribute_region_list = m.get('DistributeRegionList')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DistributeImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DistributeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DistributeImageResponseBody = None,
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
            temp_model = DistributeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DowngradeAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        auto_pay: bool = None,
        instance_group_id: str = None,
    ):
        # The IDs of the cloud phone instances that you want to delete.
        self.android_instance_ids = android_instance_ids
        # Specifies whether to enable the auto-payment feature. Default value: false.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-payment feature. Ensure your account has sufficient balance to use this feature.
        # *   false: disables the auto-payment feature. This requires manual payment each time you place an order.
        self.auto_pay = auto_pay
        # The ID of the instance group.
        # 
        # This parameter is required.
        self.instance_group_id = instance_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        return self


class DowngradeAndroidInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DowngradeAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DowngradeAndroidInstanceGroupResponseBody = None,
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
            temp_model = DowngradeAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EndCoordinationRequest(TeaModel):
    def __init__(
        self,
        coordinator_user_id: str = None,
        instance_id: str = None,
        owner_user_id: str = None,
    ):
        self.coordinator_user_id = coordinator_user_id
        self.instance_id = instance_id
        self.owner_user_id = owner_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinator_user_id is not None:
            result['CoordinatorUserId'] = self.coordinator_user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinatorUserId') is not None:
            self.coordinator_user_id = m.get('CoordinatorUserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        return self


class EndCoordinationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EndCoordinationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EndCoordinationResponseBody = None,
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
            temp_model = EndCoordinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpandDataVolumeRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        biz_region_id: str = None,
        node_ids: List[str] = None,
        share_data_volume: int = None,
    ):
        self.auto_pay = auto_pay
        self.biz_region_id = biz_region_id
        self.node_ids = node_ids
        self.share_data_volume = share_data_volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.share_data_volume is not None:
            result['ShareDataVolume'] = self.share_data_volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('ShareDataVolume') is not None:
            self.share_data_volume = m.get('ShareDataVolume')
        return self


class ExpandDataVolumeResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExpandDataVolumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExpandDataVolumeResponseBody = None,
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
            temp_model = ExpandDataVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchFileRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        source_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
        upload_url: str = None,
    ):
        # The IDs of the cloud phone instances.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # The path to the file that you want to pull from the cloud phone instance.
        # 
        # This parameter is required.
        self.source_file_path = source_file_path
        # The endpoint of the OSS bucket in which you want to store the pulled file.
        # 
        # >  Set the value to an internal endpoint when the cloud phone instance and the OSS bucket are in the same region to improve upload speed without incurring public traffic fees. Sample endpoint: `oss-cn-hangzhou-internal.aliyuncs.com`. For more information, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        # 
        # This parameter is required.
        self.upload_endpoint = upload_endpoint
        # The type of the storage service.
        # 
        # >  Currently, only OSS is supported.
        # 
        # This parameter is required.
        self.upload_type = upload_type
        # The OSS URL of the pulled file.
        # 
        # >  The OSS bucket name must start with "cloudphone-saved-bucket-", for example, "cloudphone-saved-bucket-example". You must also create an OSS directory to store the backup data. Set the value for UploadUrl in this format: oss://\\<BucketName>/\\<OSSDirectoryName>.
        # 
        # This parameter is required.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.source_file_path is not None:
            result['SourceFilePath'] = self.source_file_path
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('SourceFilePath') is not None:
            self.source_file_path = m.get('SourceFilePath')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')
        return self


class FetchFileResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        task_id: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FetchFileResponseBody(TeaModel):
    def __init__(
        self,
        data: List[FetchFileResponseBodyData] = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The objects that are returned.
        self.data = data
        # The ID of the request. If the request fails, share this ID with technical support to help diagnose the issue.
        self.request_id = request_id
        # The ID of the batch task.
        self.task_id = task_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = FetchFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FetchFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchFileResponseBody = None,
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
            temp_model = FetchFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCoordinationCodeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_user_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the user to whom the current instance is assigned.
        self.owner_user_id = owner_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        return self


class GenerateCoordinationCodeResponseBody(TeaModel):
    def __init__(
        self,
        coordinator_code: str = None,
        request_id: str = None,
    ):
        # The collaboration code.
        self.coordinator_code = coordinator_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinator_code is not None:
            result['CoordinatorCode'] = self.coordinator_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinatorCode') is not None:
            self.coordinator_code = m.get('CoordinatorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateCoordinationCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateCoordinationCodeResponseBody = None,
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
            temp_model = GenerateCoordinationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyPairRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        public_key_body: str = None,
    ):
        # The name of the ADB key pair.
        # 
        # This parameter is required.
        self.key_pair_name = key_pair_name
        # The public key of the ADB key pair.
        # 
        # This parameter is required.
        self.public_key_body = public_key_body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.public_key_body is not None:
            result['PublicKeyBody'] = self.public_key_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PublicKeyBody') is not None:
            self.public_key_body = m.get('PublicKeyBody')
        return self


class ImportKeyPairResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
    ):
        # The time when the ADB key pair was created.
        self.gmt_created = gmt_created
        # The ID of the ADB key pair.
        self.key_pair_id = key_pair_id
        # The name of the ADB key pair.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class ImportKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        data: ImportKeyPairResponseBodyData = None,
        request_id: str = None,
    ):
        # The object that is returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ImportKeyPairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportKeyPairResponseBody = None,
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
            temp_model = ImportKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallAppRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        instance_group_id_list: List[str] = None,
        instance_id_list: List[str] = None,
    ):
        # The IDs of the apps that you want to install.
        self.app_id_list = app_id_list
        # The IDs of the instance groups.
        self.instance_group_id_list = instance_group_id_list
        # The IDs of the cloud phone instances.
        self.instance_id_list = instance_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        if self.instance_group_id_list is not None:
            result['InstanceGroupIdList'] = self.instance_group_id_list
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        if m.get('InstanceGroupIdList') is not None:
            self.instance_group_id_list = m.get('InstanceGroupIdList')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        return self


class InstallAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class InstallAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallAppResponseBody = None,
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
            temp_model = InstallAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_group_ids: List[str] = None,
        policy_group_name: str = None,
        policy_type: str = None,
    ):
        # The maximum number of entries per page. Value range: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The IDs of the policies.
        self.policy_group_ids = policy_group_ids
        # The name of the policy.
        self.policy_group_name = policy_group_name
        self.policy_type = policy_type

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
        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicyRules(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        target: str = None,
    ):
        # The type of the rule.
        # 
        # Valid values:
        # 
        # *   prc: an application package name.
        # *   domain: a domain name.
        self.rule_type = rule_type
        # The name of the application package or domain name.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy(TeaModel):
    def __init__(
        self,
        custom_proxy: str = None,
        host_addr: str = None,
        net_redirect: str = None,
        port: str = None,
        proxy_password: str = None,
        proxy_type: str = None,
        proxy_user_name: str = None,
        rules: List[ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicyRules] = None,
    ):
        # Indicates whether a custom proxy is manually configured.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.custom_proxy = custom_proxy
        # The IPv4 address of the custom proxy.
        self.host_addr = host_addr
        # Indicates whether the network redirection feature is enabled. When this feature is enabled, network traffic is automatically redirected to the on-premises network by default.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.net_redirect = net_redirect
        # The port of the custom proxy. Valid values: 1 to 65535.
        self.port = port
        # The password of the proxy. The password must be 1 to 256 in length and cannot contain Chinese character or space characters.
        self.proxy_password = proxy_password
        # The type of the proxy protocol.
        # 
        # Valid values:
        # 
        # *   socks5.
        self.proxy_type = proxy_type
        # The username of the proxy. The name must be 1 to 256 in length and cannot contain Chinese character or space characters.
        self.proxy_user_name = proxy_user_name
        # The proxy rules.
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
        if self.custom_proxy is not None:
            result['CustomProxy'] = self.custom_proxy
        if self.host_addr is not None:
            result['HostAddr'] = self.host_addr
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_user_name is not None:
            result['ProxyUserName'] = self.proxy_user_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomProxy') is not None:
            self.custom_proxy = m.get('CustomProxy')
        if m.get('HostAddr') is not None:
            self.host_addr = m.get('HostAddr')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('ProxyUserName') is not None:
            self.proxy_user_name = m.get('ProxyUserName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class ListPolicyGroupsResponseBodyPolicyGroupModelPolicyRelatedResources(TeaModel):
    def __init__(
        self,
        android_instance_group_ids: List[str] = None,
        cloud_phone_matrix_ids: List[str] = None,
    ):
        self.android_instance_group_ids = android_instance_group_ids
        self.cloud_phone_matrix_ids = cloud_phone_matrix_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_group_ids is not None:
            result['AndroidInstanceGroupIds'] = self.android_instance_group_ids
        if self.cloud_phone_matrix_ids is not None:
            result['CloudPhoneMatrixIds'] = self.cloud_phone_matrix_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceGroupIds') is not None:
            self.android_instance_group_ids = m.get('AndroidInstanceGroupIds')
        if m.get('CloudPhoneMatrixIds') is not None:
            self.cloud_phone_matrix_ids = m.get('CloudPhoneMatrixIds')
        return self


class ListPolicyGroupsResponseBodyPolicyGroupModelWatermark(TeaModel):
    def __init__(
        self,
        watermark_color: int = None,
        watermark_custom_text: str = None,
        watermark_font_size: int = None,
        watermark_switch: str = None,
        watermark_transparency_value: int = None,
        watermark_types: List[str] = None,
    ):
        self.watermark_color = watermark_color
        self.watermark_custom_text = watermark_custom_text
        self.watermark_font_size = watermark_font_size
        self.watermark_switch = watermark_switch
        self.watermark_transparency_value = watermark_transparency_value
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_color is not None:
            result['WatermarkColor'] = self.watermark_color
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_font_size is not None:
            result['WatermarkFontSize'] = self.watermark_font_size
        if self.watermark_switch is not None:
            result['WatermarkSwitch'] = self.watermark_switch
        if self.watermark_transparency_value is not None:
            result['WatermarkTransparencyValue'] = self.watermark_transparency_value
        if self.watermark_types is not None:
            result['WatermarkTypes'] = self.watermark_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkColor') is not None:
            self.watermark_color = m.get('WatermarkColor')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkFontSize') is not None:
            self.watermark_font_size = m.get('WatermarkFontSize')
        if m.get('WatermarkSwitch') is not None:
            self.watermark_switch = m.get('WatermarkSwitch')
        if m.get('WatermarkTransparencyValue') is not None:
            self.watermark_transparency_value = m.get('WatermarkTransparencyValue')
        if m.get('WatermarkTypes') is not None:
            self.watermark_types = m.get('WatermarkTypes')
        return self


class ListPolicyGroupsResponseBodyPolicyGroupModel(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        gmt_create: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy: ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        policy_related_resources: ListPolicyGroupsResponseBodyPolicyGroupModelPolicyRelatedResources = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        watermark: ListPolicyGroupsResponseBodyPolicyGroupModelWatermark = None,
    ):
        # Specifies whether to enable the webcam redirection feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.camera_redirect = camera_redirect
        # The read/write permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: read and write.
        # *   off: read/write disabled.
        self.clipboard = clipboard
        # The time when the policy was created.
        self.gmt_create = gmt_create
        # The file transfer policy of the HTML5 client.
        # 
        # Valid values:
        # 
        # *   all: File upload and download are supported.
        # *   download: Only file download is supported.
        # *   upload: Only file upload is supported.
        # *   off: File upload or download is forbidden.
        self.html_5file_transfer = html_5file_transfer
        # The read/write permissions on the on-premises drive.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write denied.
        self.local_drive = local_drive
        # Identifies whether the resolution is locked.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.lock_resolution = lock_resolution
        # The network redirection policy.
        self.net_redirect_policy = net_redirect_policy
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The name of the policy.
        self.policy_group_name = policy_group_name
        self.policy_related_resources = policy_related_resources
        # The height of the resolution.
        self.session_resolution_height = session_resolution_height
        # The width of the resolution.
        self.session_resolution_width = session_resolution_width
        self.watermark = watermark

    def validate(self):
        if self.net_redirect_policy:
            self.net_redirect_policy.validate()
        if self.policy_related_resources:
            self.policy_related_resources.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy.to_map()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.policy_related_resources is not None:
            result['PolicyRelatedResources'] = self.policy_related_resources.to_map()
        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height
        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width
        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            temp_model = ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy()
            self.net_redirect_policy = temp_model.from_map(m['NetRedirectPolicy'])
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('PolicyRelatedResources') is not None:
            temp_model = ListPolicyGroupsResponseBodyPolicyGroupModelPolicyRelatedResources()
            self.policy_related_resources = temp_model.from_map(m['PolicyRelatedResources'])
        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')
        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')
        if m.get('Watermark') is not None:
            temp_model = ListPolicyGroupsResponseBodyPolicyGroupModelWatermark()
            self.watermark = temp_model.from_map(m['Watermark'])
        return self


class ListPolicyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        policy_group_model: List[ListPolicyGroupsResponseBodyPolicyGroupModel] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The policies.
        self.policy_group_model = policy_group_model
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.policy_group_model:
            for k in self.policy_group_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PolicyGroupModel'] = []
        if self.policy_group_model is not None:
            for k in self.policy_group_model:
                result['PolicyGroupModel'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policy_group_model = []
        if m.get('PolicyGroupModel') is not None:
            for k in m.get('PolicyGroupModel'):
                temp_model = ListPolicyGroupsResponseBodyPolicyGroupModel()
                self.policy_group_model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPolicyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyGroupsResponseBody = None,
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
            temp_model = ListPolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        new_android_instance_name: str = None,
    ):
        # The ID of the cloud phone instance.
        self.android_instance_id = android_instance_id
        # The new name of the cloud phone instance.
        # 
        # >  The name can be up to 30 characters in length. It can contain letters, digits, colons (:), underscores (_), periods (.), or hyphens (-). It must start with letters but cannot start with http:// or https://.
        self.new_android_instance_name = new_android_instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.new_android_instance_name is not None:
            result['NewAndroidInstanceName'] = self.new_android_instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('NewAndroidInstanceName') is not None:
            self.new_android_instance_name = m.get('NewAndroidInstanceName')
        return self


class ModifyAndroidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAndroidInstanceResponseBody = None,
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
            temp_model = ModifyAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        instance_group_id: str = None,
        new_instance_group_name: str = None,
        policy_group_id: str = None,
    ):
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The new name of the instance group.
        # 
        # > 
        # 
        # *   The name can be up to 30 characters in length. It can contain letters, digits, colons (:), underscores (_), periods (.), or hyphens (-). It must start with letters but cannot start with http:// or https://.
        self.new_instance_group_name = new_instance_group_name
        # The ID of the policy.
        self.policy_group_id = policy_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.new_instance_group_name is not None:
            result['NewInstanceGroupName'] = self.new_instance_group_name
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('NewInstanceGroupName') is not None:
            self.new_instance_group_name = m.get('NewInstanceGroupName')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        return self


class ModifyAndroidInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAndroidInstanceGroupResponseBody = None,
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
            temp_model = ModifyAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        description: str = None,
        icon_url: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The description of the application.
        self.description = description
        # The URL of the icon.
        self.icon_url = icon_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        return self


class ModifyAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppResponseBody = None,
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
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCloudPhoneNodeRequest(TeaModel):
    def __init__(
        self,
        new_node_name: str = None,
        node_id: str = None,
    ):
        # The name that you want to assign to the cloud phone matrix.
        self.new_node_name = new_node_name
        # The ID of the cloud phone matrix.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_node_name is not None:
            result['NewNodeName'] = self.new_node_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewNodeName') is not None:
            self.new_node_name = m.get('NewNodeName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ModifyCloudPhoneNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCloudPhoneNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCloudPhoneNodeResponseBody = None,
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
            temp_model = ModifyCloudPhoneNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDisplayConfigRequestDisplayConfig(TeaModel):
    def __init__(
        self,
        dpi: int = None,
        fps: int = None,
        lock_resolution: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.dpi = dpi
        self.fps = fps
        self.lock_resolution = lock_resolution
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dpi is not None:
            result['Dpi'] = self.dpi
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dpi') is not None:
            self.dpi = m.get('Dpi')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        return self


class ModifyDisplayConfigRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        display_config: ModifyDisplayConfigRequestDisplayConfig = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.display_config = display_config

    def validate(self):
        if self.display_config:
            self.display_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.display_config is not None:
            result['DisplayConfig'] = self.display_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('DisplayConfig') is not None:
            temp_model = ModifyDisplayConfigRequestDisplayConfig()
            self.display_config = temp_model.from_map(m['DisplayConfig'])
        return self


class ModifyDisplayConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        display_config_shrink: str = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.display_config_shrink = display_config_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.display_config_shrink is not None:
            result['DisplayConfig'] = self.display_config_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('DisplayConfig') is not None:
            self.display_config_shrink = m.get('DisplayConfig')
        return self


class ModifyDisplayConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDisplayConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDisplayConfigResponseBody = None,
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
            temp_model = ModifyDisplayConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceChargeTypeRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        charge_type: str = None,
        instance_group_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
    ):
        # Specifies whether to enable the auto-payment feature. Default value: false.
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature. Default value: false.
        self.auto_renew = auto_renew
        # The billing method. Valid values:
        # 
        # >  Currently, this operation only allows you to change the billing method from **pay-as-you-go to subscription**.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The IDs of the instance groups.
        # 
        # This parameter is required.
        self.instance_group_ids = instance_group_ids
        # The subscription duration. The unit is specified by PeriodUnit. Valid values: 1 Month, 2 Months, 3 Months, 6 Months, and 1 Year.
        self.period = period
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Month**\
        # *   **Year**\
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        return self


class ModifyInstanceChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        instance_group_ids: List[str] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceChargeTypeResponseBody = None,
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
            temp_model = ModifyInstanceChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyKeyPairNameRequest(TeaModel):
    def __init__(
        self,
        key_pair_id: str = None,
        new_key_pair_name: str = None,
    ):
        # The ID of the ADB key pair.
        # 
        # This parameter is required.
        self.key_pair_id = key_pair_id
        # The name of the ADB key pair.
        # 
        # This parameter is required.
        self.new_key_pair_name = new_key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.new_key_pair_name is not None:
            result['NewKeyPairName'] = self.new_key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('NewKeyPairName') is not None:
            self.new_key_pair_name = m.get('NewKeyPairName')
        return self


class ModifyKeyPairNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyKeyPairNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyKeyPairNameResponseBody = None,
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
            temp_model = ModifyKeyPairNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyGroupRequestNetRedirectPolicyRules(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        target: str = None,
    ):
        self.rule_type = rule_type
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ModifyPolicyGroupRequestNetRedirectPolicy(TeaModel):
    def __init__(
        self,
        custom_proxy: str = None,
        host_addr: str = None,
        net_redirect: str = None,
        port: str = None,
        proxy_password: str = None,
        proxy_type: str = None,
        proxy_user_name: str = None,
        rules: List[ModifyPolicyGroupRequestNetRedirectPolicyRules] = None,
    ):
        # Specifies whether to manually configure a custom proxy.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.custom_proxy = custom_proxy
        # The IPv4 address of the custom proxy.
        self.host_addr = host_addr
        # Specifies whether to enable network redirection.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.net_redirect = net_redirect
        # The port of the custom proxy. Valid values: 1 to 65535.
        self.port = port
        # The password of the proxy. The password must be 1 to 256 in length and cannot contain Chinese character or space characters.
        self.proxy_password = proxy_password
        # The type of the proxy protocol.
        # 
        # Valid values:
        # 
        # *   socks5.
        self.proxy_type = proxy_type
        # The username of the proxy. The name must be 1 to 256 in length and cannot contain Chinese character or space characters.
        self.proxy_user_name = proxy_user_name
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
        if self.custom_proxy is not None:
            result['CustomProxy'] = self.custom_proxy
        if self.host_addr is not None:
            result['HostAddr'] = self.host_addr
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_user_name is not None:
            result['ProxyUserName'] = self.proxy_user_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomProxy') is not None:
            self.custom_proxy = m.get('CustomProxy')
        if m.get('HostAddr') is not None:
            self.host_addr = m.get('HostAddr')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('ProxyUserName') is not None:
            self.proxy_user_name = m.get('ProxyUserName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ModifyPolicyGroupRequestNetRedirectPolicyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class ModifyPolicyGroupRequestWatermark(TeaModel):
    def __init__(
        self,
        watermark_color: int = None,
        watermark_custom_text: str = None,
        watermark_font_size: int = None,
        watermark_switch: str = None,
        watermark_transparency_value: int = None,
        watermark_types: List[str] = None,
    ):
        self.watermark_color = watermark_color
        self.watermark_custom_text = watermark_custom_text
        self.watermark_font_size = watermark_font_size
        self.watermark_switch = watermark_switch
        self.watermark_transparency_value = watermark_transparency_value
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_color is not None:
            result['WatermarkColor'] = self.watermark_color
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_font_size is not None:
            result['WatermarkFontSize'] = self.watermark_font_size
        if self.watermark_switch is not None:
            result['WatermarkSwitch'] = self.watermark_switch
        if self.watermark_transparency_value is not None:
            result['WatermarkTransparencyValue'] = self.watermark_transparency_value
        if self.watermark_types is not None:
            result['WatermarkTypes'] = self.watermark_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkColor') is not None:
            self.watermark_color = m.get('WatermarkColor')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkFontSize') is not None:
            self.watermark_font_size = m.get('WatermarkFontSize')
        if m.get('WatermarkSwitch') is not None:
            self.watermark_switch = m.get('WatermarkSwitch')
        if m.get('WatermarkTransparencyValue') is not None:
            self.watermark_transparency_value = m.get('WatermarkTransparencyValue')
        if m.get('WatermarkTypes') is not None:
            self.watermark_types = m.get('WatermarkTypes')
        return self


class ModifyPolicyGroupRequest(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy: ModifyPolicyGroupRequestNetRedirectPolicy = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        watermark: ModifyPolicyGroupRequestWatermark = None,
    ):
        # Specifies whether to enable the webcam redirection feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.camera_redirect = camera_redirect
        # The read/write permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.clipboard = clipboard
        # The file transfer policy of the Alibaba Cloud Workspace web client.
        # 
        # Valid values:
        # 
        # *   all: File upload and download are supported.
        # *   download: Only file download is supported.
        # *   upload: Only file upload is supported.
        # *   off: File upload or download is forbidden.
        self.html_5file_transfer = html_5file_transfer
        # The read/write permissions on the on-premises drive.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.local_drive = local_drive
        # Specifies whether to lock the resolution.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.lock_resolution = lock_resolution
        # The network redirection policy.
        self.net_redirect_policy = net_redirect_policy
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The name of the policy.
        self.policy_group_name = policy_group_name
        # The height of the resolution. Unit: pixels.
        self.resolution_height = resolution_height
        # The width of the resolution. Unit: pixels.
        self.resolution_width = resolution_width
        self.watermark = watermark

    def validate(self):
        if self.net_redirect_policy:
            self.net_redirect_policy.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy.to_map()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            temp_model = ModifyPolicyGroupRequestNetRedirectPolicy()
            self.net_redirect_policy = temp_model.from_map(m['NetRedirectPolicy'])
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('Watermark') is not None:
            temp_model = ModifyPolicyGroupRequestWatermark()
            self.watermark = temp_model.from_map(m['Watermark'])
        return self


class ModifyPolicyGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy_shrink: str = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        watermark_shrink: str = None,
    ):
        # Specifies whether to enable the webcam redirection feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.camera_redirect = camera_redirect
        # The read/write permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.clipboard = clipboard
        # The file transfer policy of the Alibaba Cloud Workspace web client.
        # 
        # Valid values:
        # 
        # *   all: File upload and download are supported.
        # *   download: Only file download is supported.
        # *   upload: Only file upload is supported.
        # *   off: File upload or download is forbidden.
        self.html_5file_transfer = html_5file_transfer
        # The read/write permissions on the on-premises drive.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.local_drive = local_drive
        # Specifies whether to lock the resolution.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.lock_resolution = lock_resolution
        # The network redirection policy.
        self.net_redirect_policy_shrink = net_redirect_policy_shrink
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The name of the policy.
        self.policy_group_name = policy_group_name
        # The height of the resolution. Unit: pixels.
        self.resolution_height = resolution_height
        # The width of the resolution. Unit: pixels.
        self.resolution_width = resolution_width
        self.watermark_shrink = watermark_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy_shrink is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy_shrink
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.watermark_shrink is not None:
            result['Watermark'] = self.watermark_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            self.net_redirect_policy_shrink = m.get('NetRedirectPolicy')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('Watermark') is not None:
            self.watermark_shrink = m.get('Watermark')
        return self


class ModifyPolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyGroupResponseBody = None,
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
            temp_model = ModifyPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        instance_id_list: List[str] = None,
        operate_type: str = None,
    ):
        # The ID of the app.
        self.app_id = app_id
        # The IDs of the cloud phone instances.
        self.instance_id_list = instance_id_list
        # The type of the operation.
        # 
        # Valid values:
        # 
        # *   stop: closes the app.
        # *   restart: reopens the app.
        # *   start: open the app.
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class OperateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OperateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateAppResponseBody = None,
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
            temp_model = OperateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootAndroidInstancesInGroupRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        force_stop: bool = None,
        sale_mode: str = None,
    ):
        # The IDs of the cloud phone instances.
        self.android_instance_ids = android_instance_ids
        # Specifies whether to enforce a restart operation. If a cloud phone instance fails to stop due to system or network issues, a forced restart can be triggered, though it may result in data loss.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.force_stop = force_stop
        self.sale_mode = sale_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        return self


class RebootAndroidInstancesInGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootAndroidInstancesInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootAndroidInstancesInGroupResponseBody = None,
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
            temp_model = RebootAndroidInstancesInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryFileRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_all: bool = None,
        backup_file_id: str = None,
        backup_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # The IDs of the instances.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # Specifies whether to back up the whole instance.
        self.backup_all = backup_all
        # The ID of the backup file.
        self.backup_file_id = backup_file_id
        # The OSS path to which the backup file is uploaded.
        # 
        # >  When calling the describeBuckets operation to retrieve a bucket name, you must also call the ossObjectList operation to obtain the object key. Combine these to form the full path: oss://${bucketName}/${key}.
        self.backup_file_path = backup_file_path
        # The endpoint of the OSS bucket that stores the backup file.
        # 
        # > : When calling the DescribeBuckets operation to query buckets, retrieve the IntranetEndpoint value if the cloud phone and the OSS bucket are in the same region. If they are in different regions, retrieve the ExtranetEndpoint value instead.
        self.upload_endpoint = upload_endpoint
        # The type of the backup.
        # 
        # Valid values:
        # 
        # *   OSS: backup files are stored in OSS buckets.
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.backup_all is not None:
            result['BackupAll'] = self.backup_all
        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id
        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('BackupAll') is not None:
            self.backup_all = m.get('BackupAll')
        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')
        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class RecoveryFileResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        task_id: str = None,
    ):
        # The instance ID.
        self.android_instance_id = android_instance_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RecoveryFileResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        data: List[RecoveryFileResponseBodyData] = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The number of restored instances.
        self.count = count
        # The backup file that is restored.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # The ID of the batch task.
        self.task_id = task_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = RecoveryFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RecoveryFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoveryFileResponseBody = None,
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
            temp_model = RecoveryFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAndroidInstanceGroupsRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        instance_group_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-payment feature. Ensure your account has sufficient balance to use this feature.
        # *   false: disables the auto-payment feature. You need to manually complete the payment process.
        self.auto_pay = auto_pay
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The duration of the renewal, measured in units defined by PeriodUnit.
        self.period = period
        # The unit of the renewal duration. Default value: Month.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        return self


class RenewAndroidInstanceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewAndroidInstanceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewAndroidInstanceGroupsResponseBody = None,
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
            temp_model = RenewAndroidInstanceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewCloudPhoneNodesRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        node_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
    ):
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-renewal feature. In this case, the system automatically renews the instance upon expiration.
        # *   false (default): disables the auto-renewal feature. In this case, you need to manually renew the instance upon expiration.
        self.auto_renew = auto_renew
        # The cloud phone matrix IDs.
        self.node_ids = node_ids
        # The subscription duration. The unit is specified by `PeriodUnit`. Valid values:
        # 
        # *   When `PeriodUnit` is set to **year**: 1.
        # *   When `PeriodUnit` is set to **month**: 1, 2, 3, and 6.
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month (default)
        # *   Year
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        return self


class RenewCloudPhoneNodesResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewCloudPhoneNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewCloudPhoneNodesResponseBody = None,
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
            temp_model = RenewCloudPhoneNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAndroidInstancesInGroupRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        sale_mode: str = None,
        setting_reset_type: int = None,
    ):
        # The IDs of the cloud phone instances.
        self.android_instance_ids = android_instance_ids
        self.sale_mode = sale_mode
        self.setting_reset_type = setting_reset_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.setting_reset_type is not None:
            result['SettingResetType'] = self.setting_reset_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('SettingResetType') is not None:
            self.setting_reset_type = m.get('SettingResetType')
        return self


class ResetAndroidInstancesInGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAndroidInstancesInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAndroidInstancesInGroupResponseBody = None,
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
            temp_model = ResetAndroidInstancesInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        content_encoding: str = None,
        instance_ids: List[str] = None,
        timeout: int = None,
    ):
        # The content of the command.
        self.command_content = command_content
        # The encoding method of the command content (`CommandContent`). The value is not case-sensitive.
        # 
        # >  If you set the value to an invalid encoding method, the system will process the command content as `PlainText`.
        # 
        # Valid values:
        # 
        # *   Base64: encodes the command content in Base64.
        # *   PlainText (default): does not encode the command content. The command content is input as plain text.
        self.content_encoding = content_encoding
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        self.instance_ids = instance_ids
        # The timeout period of the command execution. If the command execution exceeds the timeout period, it will be considered timed out. If you leave this parameter empty, it defaults to 60.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        # The ID of the command execution. You can use the command execution ID to query the output of a command.
        self.invoke_id = invoke_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCommandResponseBody = None,
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
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendFileRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        source_file_path: str = None,
        target_file_name: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
        upload_url: str = None,
    ):
        # The IDs of the cloud phone instances.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # The path to which you want to upload the pushed file in the cloud phone instance.
        # 
        # This parameter is required.
        self.source_file_path = source_file_path
        # The name of the file uploaded from the Object Storage Service (OSS) to the cloud phone instance.
        # 
        # >  If UploadType is set to OSS, you must specify TargetFileName. If TargetFileName is empty, the file uploaded from the OSS bucket to the cloud phone instance retains its original name. If TargetFileName is provided with a value, the uploaded file in the SourceFilePath directory uses the specified name (TargetFileName). If UploadType is set to DOWNLOAD_URL, TargetFileName does not take effect.
        self.target_file_name = target_file_name
        # The endpoint of the OSS bucket in which the file is stored.
        # 
        # >  Set the value to an internal endpoint when the cloud phone instance and the OSS bucket are in the same region to improve transfer speed without incurring public traffic fees. Sample endpoint: `oss-cn-hangzhou-internal.aliyuncs.com`. For more information, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        self.upload_endpoint = upload_endpoint
        # The storage type of the file that you want to upload.
        # 
        # *   Set the value to OSS.
        # 
        # This parameter is required.
        self.upload_type = upload_type
        # The OSS URL of the file.
        # 
        # >  The OSS bucket name must start with "cloudphone-saved-bucket-", for example, "cloudphone-saved-bucket-example". You must also create an OSS directory to store the backup data. Set the value for UploadUrl in this format: oss://\\<BucketName>/\\<OSSDirectoryName>\\<FileName>.
        # 
        # This parameter is required.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.source_file_path is not None:
            result['SourceFilePath'] = self.source_file_path
        if self.target_file_name is not None:
            result['TargetFileName'] = self.target_file_name
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('SourceFilePath') is not None:
            self.source_file_path = m.get('SourceFilePath')
        if m.get('TargetFileName') is not None:
            self.target_file_name = m.get('TargetFileName')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')
        return self


class SendFileResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        task_id: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SendFileResponseBody(TeaModel):
    def __init__(
        self,
        data: List[SendFileResponseBodyData] = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The objects that are returned.
        self.data = data
        # The ID of the request. If the request fails, share this ID with technical support to help diagnose the issue.
        self.request_id = request_id
        # The ID of the batch task.
        self.task_id = task_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SendFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SendFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendFileResponseBody = None,
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
            temp_model = SendFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAdbSecureRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        status: int = None,
    ):
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        self.instance_ids = instance_ids
        # The status of the ADB authentication feature.
        # 
        # Valid values:
        # 
        # *   0: The ADB authentication feature is disabled.
        # *   1: The ADB authentication feature is enabled.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetAdbSecureResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_count: int = None,
        instance_ids: List[str] = None,
        total_count: int = None,
    ):
        # The number of the cloud phone instances for which the ADB authentication feature failed to be enabled.
        self.fail_count = fail_count
        # The IDs of the cloud phone instances for which the ADB authentication feature is enabled.
        self.instance_ids = instance_ids
        # The total number of the cloud phone instances.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SetAdbSecureResponseBody(TeaModel):
    def __init__(
        self,
        data: SetAdbSecureResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned object.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SetAdbSecureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetAdbSecureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetAdbSecureResponseBody = None,
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
            temp_model = SetAdbSecureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        sale_mode: str = None,
    ):
        # List of instances.
        self.android_instance_ids = android_instance_ids
        self.sale_mode = sale_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        return self


class StartAndroidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAndroidInstanceResponseBody = None,
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
            temp_model = StartAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        force_stop: bool = None,
        sale_mode: str = None,
    ):
        # The IDs of the cloud phone instances.
        self.android_instance_ids = android_instance_ids
        # Specifies whether to enforce a stop operation. If a cloud phone instance fails to stop due to system or network issues, a forced stop can be triggered, though it may result in data loss.
        self.force_stop = force_stop
        self.sale_mode = sale_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        return self


class StopAndroidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAndroidInstanceResponseBody = None,
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
            temp_model = StopAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallAppRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        instance_group_id_list: List[str] = None,
        instance_id_list: List[str] = None,
    ):
        # The IDs of the apps.
        self.app_id_list = app_id_list
        # The ID of the instance groups. If you specify this parameter, you cannot specify InstanceIdList.
        self.instance_group_id_list = instance_group_id_list
        # The IDs of the cloud phone instances. If you specify this parameter, you cannot specify InstanceGroupIdList.
        self.instance_id_list = instance_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        if self.instance_group_id_list is not None:
            result['InstanceGroupIdList'] = self.instance_group_id_list
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        if m.get('InstanceGroupIdList') is not None:
            self.instance_group_id_list = m.get('InstanceGroupIdList')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        return self


class UninstallAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UninstallAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallAppResponseBody = None,
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
            temp_model = UninstallAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomImageNameRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
    ):
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class UpdateCustomImageNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCustomImageNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomImageNameResponseBody = None,
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
            temp_model = UpdateCustomImageNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceGroupImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        instance_group_ids: List[str] = None,
    ):
        # The ID of the image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The IDs of the instance groups.
        # 
        # This parameter is required.
        self.instance_group_ids = instance_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        return self


class UpdateInstanceGroupImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceGroupImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceGroupImageResponseBody = None,
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
            temp_model = UpdateInstanceGroupImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        instance_id_list: List[str] = None,
    ):
        self.image_id = image_id
        self.instance_id_list = instance_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        return self


class UpdateInstanceImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateInstanceImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceImageResponseBody = None,
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
            temp_model = UpdateInstanceImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        increase_number_of_instance: int = None,
        instance_group_id: str = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-payment feature. Make sure that your Alibaba Cloud account has sufficient balance.
        # *   false: disables the auto-payment feature. You need to manually complete the payment process.
        self.auto_pay = auto_pay
        # The number of instances that you want to increase.
        self.increase_number_of_instance = increase_number_of_instance
        # The ID of the instance group.
        self.instance_group_id = instance_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.increase_number_of_instance is not None:
            result['IncreaseNumberOfInstance'] = self.increase_number_of_instance
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('IncreaseNumberOfInstance') is not None:
            self.increase_number_of_instance = m.get('IncreaseNumberOfInstance')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        return self


class UpgradeAndroidInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.instance_ids = instance_ids
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeAndroidInstanceGroupResponseBody = None,
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
            temp_model = UpgradeAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


