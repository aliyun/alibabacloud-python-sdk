# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeJobResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The information of the job template.
        self.data = data
        # The error code returned. Take note of the following rules:
        # 
        # *   If the call is successful, **ErrorCode** is not returned.
        # *   If the call fails, **ErrorCode** is returned. For more information, see the "**Error codes**" section in this topic.
        self.error_code = error_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the configurations of the job template were obtained. Valid values:
        # 
        # *   **true**: The configurations were obtained.
        # *   **false**: The configurations failed to be obtained.
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeJobResponseBodyData(DaraModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        backoff_limit: int = None,
        best_effort_type: str = None,
        command: str = None,
        command_args: str = None,
        concurrency_policy: str = None,
        config_map_mount_desc: List[main_models.DescribeJobResponseBodyDataConfigMapMountDesc] = None,
        cpu: int = None,
        custom_host_alias: str = None,
        edas_container_version: str = None,
        envs: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        memory: int = None,
        mount_desc: List[main_models.DescribeJobResponseBodyDataMountDesc] = None,
        mount_host: str = None,
        namespace_id: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: List[main_models.DescribeJobResponseBodyDataOssMountDescs] = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        programming_language: str = None,
        public_web_hook_urls: List[str] = None,
        python: str = None,
        python_modules: str = None,
        ref_app_id: str = None,
        refed_app_ids: List[str] = None,
        region_id: str = None,
        replicas: int = None,
        security_group_id: str = None,
        slice: bool = None,
        slice_envs: str = None,
        sls_configs: str = None,
        suspend: bool = None,
        tags: List[main_models.DescribeJobResponseBodyDataTags] = None,
        termination_grace_period_seconds: int = None,
        timeout: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        trigger_config: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_web_hook_urls: List[str] = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is used to pull images across accounts. For more information, see [Pull images across Alibaba Cloud accounts](https://help.aliyun.com/document_detail/190675.html) and [Grant permissions across Alibaba Cloud accounts by using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The ID of the Container Registry Enterprise Edition instance.
        self.acr_instance_id = acr_instance_id
        # The description of the job template.
        self.app_description = app_description
        # The ID of the job template.
        self.app_id = app_id
        # The name of the job template.
        self.app_name = app_name
        # The number of times that the job was retried.
        self.backoff_limit = backoff_limit
        self.best_effort_type = best_effort_type
        # The command that is used to start the image. The command must be an existing executable object in the container. Example:
        # 
        #     command:
        #           - echo
        #           - abc
        #           - >
        #           - file0
        # 
        # In this example, the Command parameter is set to `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The arguments of the image startup command. This parameter contains the arguments that are required for **Command**. Format:
        # 
        # `["a","b"]`
        # 
        # In the preceding **Command** example, the CommandArgs parameter is set to `CommandArgs=["abc", ">", "file0"]`. The data type of `["abc", ">", "file0"]` must be an array of strings in the JSON format. If this parameter does not exist in the Command parameter, you do not need to configure it.
        self.command_args = command_args
        # The concurrency policy of the job. Valid values:
        # 
        # *   **Forbid**: Concurrent running is prohibited. If the previous job is not completed, no new job is created.
        # *   **Allow**: Concurrent running is allowed.
        # *   **Replace**: If the previous job is not completed when the time to create a new job is reached, the new job replaces the previous job.
        self.concurrency_policy = concurrency_policy
        # The details of the ConfigMap.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU specifications required for each instance. Unit: millicore. This parameter cannot be set to 0. Valid values:
        # 
        # *   **500**
        # *   **1000**
        # *   **2000**
        # *   **4000**
        # *   **8000**
        # *   **16000**
        # *   **32000**
        self.cpu = cpu
        # The custom mapping between the hostname and IP address in the container. Valid values:
        # 
        # *   **hostName**: the domain name or hostname.
        # *   **ip**: the IP address.
        self.custom_host_alias = custom_host_alias
        # The version of the container, such as Ali-Tomcat, in which a job that is developed based on High-speed Service Framework (HSF) is deployed.
        self.edas_container_version = edas_container_version
        # The environment variables. You can configure custom environment variables or reference a ConfigMap. If you want to reference a ConfigMap, you must first create a ConfigMap. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Valid values:
        # 
        # *   Custom configuration
        # 
        #     *   **name**: the name of the environment variable.
        #     *   **value**: the value of the environment variable.
        # 
        # *   Reference a ConfigMap
        # 
        #     *   **name**: the name of the environment variable. You can reference one or all keys. To reference all keys, specify `sae-sys-configmap-all-<ConfigMap name>`. Example: `sae-sys-configmap-all-test1`.
        #     *   **valueFrom**: the reference of the environment variable. Set the value to `configMapRef`.
        #     *   **configMapId**: the ID of the ConfigMap.
        #     *   **key**: the key. If you want to reference all keys, you do not need to configure this parameter.
        self.envs = envs
        # The ID of the corresponding secret.
        self.image_pull_secrets = image_pull_secrets
        # The URL of the image. This parameter is returned only if **PackageType** is set to **Image**.
        self.image_url = image_url
        # The arguments in the JAR package. The arguments are used to start the job. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_args = jar_start_args
        # The option settings in the JAR package. The settings are used to start the job. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_options = jar_start_options
        # The version of the Java Development Kit (JDK) on which the deployment package of the application depends. The following versions are supported:
        # 
        # *   **Open JDK 8**
        # *   **Open JDK 7**
        # *   **Dragonwell 11**
        # *   **Dragonwell 8**
        # *   **openjdk-8u191-jdk-alpine3.9**
        # *   **openjdk-7u201-jdk-alpine3.9**
        # 
        # This parameter is not returned if **PackageType** is set to **Image**.
        self.jdk = jdk
        # The size of memory that is required by each instance. Unit: MB. This parameter cannot be set to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   This parameter is set to **1024** if the Cpu parameter is set to 500 or 1000.
        # *   This parameter is set to **2048** if the Cpu parameter is set to 500, 1000, or 2000.
        # *   This parameter is set to **4096** if the Cpu parameter is set to 1000, 2000, or 4000.
        # *   This parameter is set to **8192** if the Cpu parameter is set to 2000, 4000, or 8000.
        # *   This parameter is set to **12288** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **16384** if the Cpu parameter is set to 4000, 8000, or 16000.
        # *   This parameter is set to **24567** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **32768** if the Cpu parameter is set to 16000.
        # *   This parameter is set to **65536** if the Cpu parameter is set to 8000, 16000, or 32000.
        # *   This parameter is set to **131072** if the Cpu parameter is set to 32000.
        self.memory = memory
        # The details of the mounted NAS file system.
        self.mount_desc = mount_desc
        # The mount target of the Apsara File Storage NAS (NAS) file system in the virtual private cloud (VPC) where the job template is deployed. If you do not need to modify the NAS configurations when you deploy the job template, configure the **MountHost** parameter only in the first request. You do not need to include this parameter in subsequent requests. If you no longer need to use NAS, leave the **MountHost** parameter empty in the request.
        self.mount_host = mount_host
        # The namespace ID.
        self.namespace_id = namespace_id
        # The configurations for mounting the NAS file system.
        self.nas_configs = nas_configs
        # The ID of the NAS file system.
        self.nas_id = nas_id
        # The AccessKey ID that is used to read data from and write data to Object Storage Service (OSS).
        self.oss_ak_id = oss_ak_id
        # The AccessKey secret that is used to read data from and write data to OSS.
        self.oss_ak_secret = oss_ak_secret
        # The description of mounted OSS buckets.
        self.oss_mount_descs = oss_mount_descs
        # The type of the deployment package. Valid values:
        # 
        # *   If you deploy a Java job template, you can set this parameter to **FatJar**, **War**, or **Image**.
        # 
        # *   If you deploy a PHP job template, the following types are available:
        # 
        #     *   **PhpZip**
        #     *   **IMAGE_PHP_5_4**
        #     *   **IMAGE_PHP_5_4_ALPINE**
        #     *   **IMAGE_PHP_5_5**
        #     *   **IMAGE_PHP_5_5_ALPINE**
        #     *   **IMAGE_PHP_5_6**
        #     *   **IMAGE_PHP_5_6_ALPINE**
        #     *   **IMAGE_PHP_7_0**
        #     *   **IMAGE_PHP_7_0_ALPINE**
        #     *   **IMAGE_PHP_7_1**
        #     *   **IMAGE_PHP_7_1_ALPINE**
        #     *   **IMAGE_PHP_7_2**
        #     *   **IMAGE_PHP_7_2_ALPINE**
        #     *   **IMAGE_PHP_7_3**
        #     *   **IMAGE_PHP_7_3_ALPINE**
        # 
        # *   If you deploy a Python job template, you can set this parameter to **PythonZip** or **Image**.
        self.package_type = package_type
        # The URL of the deployment package. This parameter is returned only if **PackageType** is set to **FatJar** or **War**.
        self.package_url = package_url
        # The version of the deployment package. This parameter is required only if **PackageType** is set to **FatJar** or **War**.
        self.package_version = package_version
        # The details of the PHP configuration file.
        self.php_config = php_config
        # The path on which the PHP configuration file for job startup is mounted. Make sure that the PHP server uses this configuration file during the startup.
        self.php_config_location = php_config_location
        # The script that is run immediately after the container is started. Example: `{"exec":{"command":["cat","/etc/group"\\]}}`
        self.post_start = post_start
        # The script that is run before the container is stopped. Example: `{"exec":{"command":["cat","/etc/group"\\]}}`
        self.pre_stop = pre_stop
        # The programming language in which the job template is created. Valid values:
        # 
        # *   **java**: Java
        # *   **php**: PHP
        # *   **python**: Python
        # *   **other**: other programming languages, such as C++, Go, .NET, and Node.js
        self.programming_language = programming_language
        # The Internet request URLs of one-time jobs.
        self.public_web_hook_urls = public_web_hook_urls
        # The Python environment. PYTHON 3.9.15 is supported.
        self.python = python
        # The configurations for installing custom module dependencies. By default, the dependencies defined by the requirements.txt file in the root directory are installed. If no software package is configured, you can specify dependencies based on your business requirements.
        self.python_modules = python_modules
        # The ID of the job template that you reference.
        self.ref_app_id = ref_app_id
        # The IDs of the referenced job templates.
        self.refed_app_ids = refed_app_ids
        # The region ID.
        self.region_id = region_id
        # The number of job instances.
        self.replicas = replicas
        # The ID of the security group.
        self.security_group_id = security_group_id
        # Indicates whether job sharding is enabled.
        self.slice = slice
        # The parameters of job sharding.
        self.slice_envs = slice_envs
        # The logging configurations of Log Service.
        # 
        # *   To use Log Service resources that are automatically created by SAE, set this parameter to `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # *   To use custom Log Service resources, set this parameter to `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # Parameter description:
        # 
        # *   **projectName**: the name of the Log Service project.
        # *   **logDir**: the path in which logs are stored.
        # *   **logType**: the log type. **stdout**: the standard output (stdout) log of the container. Only one stdout value for this parameter can be specified. If this parameter is not configured, file logs are collected.
        # *   **logstoreName**: the name of the Logstore in Log Service.
        # *   **logtailName**: the name of the Logtail in Log Service. If this parameter is not configured, a new Logtail is created.
        # 
        # If you do not need to modify the logging configurations when you deploy the application, configure **SlsConfigs** only in the first request. If you no longer need to use Log Service, leave **SlsConfigs** empty in the request.
        self.sls_configs = sls_configs
        # Indicates whether the job template is suspended.
        self.suspend = suspend
        # The tags.
        self.tags = tags
        # The timeout period for a graceful shutdown. Default value: 30. Unit: seconds. Valid values: 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The timeout period of the job. Unit: seconds.
        self.timeout = timeout
        # The time zone. Default value: **Asia/Shanghai**.
        self.timezone = timezone
        # The Tomcat configuration. If you want to delete the configuration, set this parameter to {} or leave this parameter empty. Parameter description:
        # 
        # *   **port**: the port number. Valid values: 1024 to 65535. The root permissions are required to perform operations on ports whose number is smaller than 1024. Enter a value that ranges from 1025 to 65535 because the container has only the admin permissions. If this parameter is not configured, the default value 8080 is used.
        # *   **contextPath**: the path. Default value: /. The value indicates the root directory.
        # *   **maxThreads**: the maximum number of connections in the connection pool. Default value: 400.
        # *   **uriEncoding**: the URI encoding scheme in the Tomcat container. Valid values: **UTF-8**, **ISO-8859-1**, **GBK**, and **GB2312**. If this parameter is not configured, the default value **ISO-8859-1** is used.
        # *   **useBodyEncoding**: indicates whether to use the encoding scheme that is specified by **BodyEncoding for URL**. Default value: **true**.
        self.tomcat_config = tomcat_config
        self.trigger_config = trigger_config
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The internal request URLs for one-time jobs.
        self.vpc_web_hook_urls = vpc_web_hook_urls
        # The option settings in the WAR package. The settings are used to start the job. The default startup command is `java $JAVA_OPTS $CATALINA_OPTS -Options org.apache.catalina.startup.Bootstrap "$@" start`.
        self.war_start_options = war_start_options
        # The version of the Tomcat container on which the deployment package depends. The following versions are supported:
        # 
        # *   **apache-tomcat-7.0.91**
        # *   **apache-tomcat-8.5.42**
        # 
        # This parameter is not returned if **PackageType** is set to **Image**.
        self.web_container = web_container

    def validate(self):
        if self.config_map_mount_desc:
            for v1 in self.config_map_mount_desc:
                 if v1:
                    v1.validate()
        if self.mount_desc:
            for v1 in self.mount_desc:
                 if v1:
                    v1.validate()
        if self.oss_mount_descs:
            for v1 in self.oss_mount_descs:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn

        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id

        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.backoff_limit is not None:
            result['BackoffLimit'] = self.backoff_limit

        if self.best_effort_type is not None:
            result['BestEffortType'] = self.best_effort_type

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        if self.concurrency_policy is not None:
            result['ConcurrencyPolicy'] = self.concurrency_policy

        result['ConfigMapMountDesc'] = []
        if self.config_map_mount_desc is not None:
            for k1 in self.config_map_mount_desc:
                result['ConfigMapMountDesc'].append(k1.to_map() if k1 else None)

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args

        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options

        if self.jdk is not None:
            result['Jdk'] = self.jdk

        if self.memory is not None:
            result['Memory'] = self.memory

        result['MountDesc'] = []
        if self.mount_desc is not None:
            for k1 in self.mount_desc:
                result['MountDesc'].append(k1.to_map() if k1 else None)

        if self.mount_host is not None:
            result['MountHost'] = self.mount_host

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.nas_configs is not None:
            result['NasConfigs'] = self.nas_configs

        if self.nas_id is not None:
            result['NasId'] = self.nas_id

        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id

        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret

        result['OssMountDescs'] = []
        if self.oss_mount_descs is not None:
            for k1 in self.oss_mount_descs:
                result['OssMountDescs'].append(k1.to_map() if k1 else None)

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.php_config is not None:
            result['PhpConfig'] = self.php_config

        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language

        if self.public_web_hook_urls is not None:
            result['PublicWebHookUrls'] = self.public_web_hook_urls

        if self.python is not None:
            result['Python'] = self.python

        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules

        if self.ref_app_id is not None:
            result['RefAppId'] = self.ref_app_id

        if self.refed_app_ids is not None:
            result['RefedAppIds'] = self.refed_app_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.slice is not None:
            result['Slice'] = self.slice

        if self.slice_envs is not None:
            result['SliceEnvs'] = self.slice_envs

        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs

        if self.suspend is not None:
            result['Suspend'] = self.suspend

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config

        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_web_hook_urls is not None:
            result['VpcWebHookUrls'] = self.vpc_web_hook_urls

        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')

        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BackoffLimit') is not None:
            self.backoff_limit = m.get('BackoffLimit')

        if m.get('BestEffortType') is not None:
            self.best_effort_type = m.get('BestEffortType')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        if m.get('ConcurrencyPolicy') is not None:
            self.concurrency_policy = m.get('ConcurrencyPolicy')

        self.config_map_mount_desc = []
        if m.get('ConfigMapMountDesc') is not None:
            for k1 in m.get('ConfigMapMountDesc'):
                temp_model = main_models.DescribeJobResponseBodyDataConfigMapMountDesc()
                self.config_map_mount_desc.append(temp_model.from_map(k1))

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')

        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')

        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        self.mount_desc = []
        if m.get('MountDesc') is not None:
            for k1 in m.get('MountDesc'):
                temp_model = main_models.DescribeJobResponseBodyDataMountDesc()
                self.mount_desc.append(temp_model.from_map(k1))

        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NasConfigs') is not None:
            self.nas_configs = m.get('NasConfigs')

        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')

        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')

        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')

        self.oss_mount_descs = []
        if m.get('OssMountDescs') is not None:
            for k1 in m.get('OssMountDescs'):
                temp_model = main_models.DescribeJobResponseBodyDataOssMountDescs()
                self.oss_mount_descs.append(temp_model.from_map(k1))

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')

        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')

        if m.get('PublicWebHookUrls') is not None:
            self.public_web_hook_urls = m.get('PublicWebHookUrls')

        if m.get('Python') is not None:
            self.python = m.get('Python')

        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')

        if m.get('RefAppId') is not None:
            self.ref_app_id = m.get('RefAppId')

        if m.get('RefedAppIds') is not None:
            self.refed_app_ids = m.get('RefedAppIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Slice') is not None:
            self.slice = m.get('Slice')

        if m.get('SliceEnvs') is not None:
            self.slice_envs = m.get('SliceEnvs')

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('Suspend') is not None:
            self.suspend = m.get('Suspend')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeJobResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')

        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcWebHookUrls') is not None:
            self.vpc_web_hook_urls = m.get('VpcWebHookUrls')

        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        return self

class DescribeJobResponseBodyDataTags(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeJobResponseBodyDataOssMountDescs(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        # The name of the bucket.
        self.bucket_name = bucket_name
        # The directory or object in OSS. If the specified directory or object does not exist, an error is returned.
        self.bucket_path = bucket_path
        # The path of the container in SAE. The parameter value that you specified overwrites the original value. If the specified path does not exist, SAE automatically creates the path.
        self.mount_path = mount_path
        # Indicates whether the job template can use the container directory to read data from or write data to resources in the directory of the OSS bucket. Valid values:
        # 
        # *   **true**: The job template has the read-only permissions.
        # *   **false**: The job template has the read and write permissions.
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path

        if self.mount_path is not None:
            result['mountPath'] = self.mount_path

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')

        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        return self

class DescribeJobResponseBodyDataMountDesc(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        nas_path: str = None,
    ):
        # The path on which the NAS file system is mounted.
        self.mount_path = mount_path
        # The directory in the NAS file system.
        self.nas_path = nas_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.nas_path is not None:
            result['NasPath'] = self.nas_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')

        return self

class DescribeJobResponseBodyDataConfigMapMountDesc(DaraModel):
    def __init__(
        self,
        config_map_id: int = None,
        config_map_name: str = None,
        key: str = None,
        mount_path: str = None,
    ):
        # The ConfigMap ID.
        self.config_map_id = config_map_id
        # The ConfigMap name.
        self.config_map_name = config_map_name
        # The key-value pair that is stored in the ConfigMap.
        self.key = key
        # The path on which the ConfigMap is mounted.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id

        if self.config_map_name is not None:
            result['ConfigMapName'] = self.config_map_name

        if self.key is not None:
            result['Key'] = self.key

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')

        if m.get('ConfigMapName') is not None:
            self.config_map_name = m.get('ConfigMapName')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

