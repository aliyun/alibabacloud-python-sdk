# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudbenchTaskConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeCloudbenchTaskConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information, including the error codes and the number of entries that are returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
            temp_model = main_models.DescribeCloudbenchTaskConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCloudbenchTaskConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        archive_folder: str = None,
        bench_cmd: str = None,
        client_jar_path: str = None,
        jar_on_oss: str = None,
        load_cmd: str = None,
        meta_file_name: str = None,
        meta_file_on_oss: str = None,
        meta_file_path: str = None,
        parse_cmd: str = None,
        parse_file_path: str = None,
        rocks_db_path: str = None,
        sql_file_name: str = None,
        sql_file_on_oss: str = None,
        sql_file_path: str = None,
        task_id: str = None,
        user_id: str = None,
        work_dir: str = None,
    ):
        # The path in which the files are archived.
        self.archive_folder = archive_folder
        # The command that was run to start the stress testing task.
        self.bench_cmd = bench_cmd
        # The path to the JAR file that is used for stress testing.
        self.client_jar_path = client_jar_path
        # The path to the JAR file that is stored in OSS. The JAR file is used for stress testing.
        self.jar_on_oss = jar_on_oss
        # The command that was run to preload the file that stores the analysis result of full SQL statistics.
        self.load_cmd = load_cmd
        # The name of the metadata file.
        self.meta_file_name = meta_file_name
        # The name of the metadata file stored in Object Storage Service (OSS).
        self.meta_file_on_oss = meta_file_on_oss
        # The path to the metadata file.
        self.meta_file_path = meta_file_path
        # The command that was run to parse the file that stores the analysis result of full SQL statistics.
        self.parse_cmd = parse_cmd
        # The path to the file that is parsed. The file stores the analysis result of full SQL statistics.
        self.parse_file_path = parse_file_path
        # The location where the RocksDB storage system is deployed in the stress testing client.
        self.rocks_db_path = rocks_db_path
        # The name of the file that stores the analysis result of full SQL statistics.
        self.sql_file_name = sql_file_name
        # The name of the file that stores the analysis result of full SQL statistics and that is stored in OSS.
        self.sql_file_on_oss = sql_file_on_oss
        # The path to the file that stores the analysis result of full SQL statistics.
        self.sql_file_path = sql_file_path
        # The task ID.
        self.task_id = task_id
        # The Alibaba Cloud account ID.
        self.user_id = user_id
        # The path of the temporary directory that is generated for stress testing.
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_folder is not None:
            result['ArchiveFolder'] = self.archive_folder

        if self.bench_cmd is not None:
            result['BenchCmd'] = self.bench_cmd

        if self.client_jar_path is not None:
            result['ClientJarPath'] = self.client_jar_path

        if self.jar_on_oss is not None:
            result['JarOnOss'] = self.jar_on_oss

        if self.load_cmd is not None:
            result['LoadCmd'] = self.load_cmd

        if self.meta_file_name is not None:
            result['MetaFileName'] = self.meta_file_name

        if self.meta_file_on_oss is not None:
            result['MetaFileOnOss'] = self.meta_file_on_oss

        if self.meta_file_path is not None:
            result['MetaFilePath'] = self.meta_file_path

        if self.parse_cmd is not None:
            result['ParseCmd'] = self.parse_cmd

        if self.parse_file_path is not None:
            result['ParseFilePath'] = self.parse_file_path

        if self.rocks_db_path is not None:
            result['RocksDbPath'] = self.rocks_db_path

        if self.sql_file_name is not None:
            result['SqlFileName'] = self.sql_file_name

        if self.sql_file_on_oss is not None:
            result['SqlFileOnOss'] = self.sql_file_on_oss

        if self.sql_file_path is not None:
            result['SqlFilePath'] = self.sql_file_path

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveFolder') is not None:
            self.archive_folder = m.get('ArchiveFolder')

        if m.get('BenchCmd') is not None:
            self.bench_cmd = m.get('BenchCmd')

        if m.get('ClientJarPath') is not None:
            self.client_jar_path = m.get('ClientJarPath')

        if m.get('JarOnOss') is not None:
            self.jar_on_oss = m.get('JarOnOss')

        if m.get('LoadCmd') is not None:
            self.load_cmd = m.get('LoadCmd')

        if m.get('MetaFileName') is not None:
            self.meta_file_name = m.get('MetaFileName')

        if m.get('MetaFileOnOss') is not None:
            self.meta_file_on_oss = m.get('MetaFileOnOss')

        if m.get('MetaFilePath') is not None:
            self.meta_file_path = m.get('MetaFilePath')

        if m.get('ParseCmd') is not None:
            self.parse_cmd = m.get('ParseCmd')

        if m.get('ParseFilePath') is not None:
            self.parse_file_path = m.get('ParseFilePath')

        if m.get('RocksDbPath') is not None:
            self.rocks_db_path = m.get('RocksDbPath')

        if m.get('SqlFileName') is not None:
            self.sql_file_name = m.get('SqlFileName')

        if m.get('SqlFileOnOss') is not None:
            self.sql_file_on_oss = m.get('SqlFileOnOss')

        if m.get('SqlFilePath') is not None:
            self.sql_file_path = m.get('SqlFilePath')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        return self

