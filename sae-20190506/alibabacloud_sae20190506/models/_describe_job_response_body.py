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
        # The HTTP status code or POP error code. Valid values:
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: A request error occurred.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The job template information.
        self.data = data
        # The error code.
        # 
        # - The **ErrorCode** parameter is returned only if the request fails.
        # 
        # - For a list of possible **ErrorCode** values, see the **Error codes** section in this topic.
        self.error_code = error_code
        # Additional information about the call result.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The trace ID used to query the details of a request.
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
        # The ARN of the RAM role that is required to pull images across accounts. For more information, see [Pull images across Alibaba Cloud accounts](https://help.aliyun.com/document_detail/190675.html) and [Grant permissions across Alibaba Cloud accounts by using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The ID of the Container Registry (ACR) Enterprise Edition instance.
        self.acr_instance_id = acr_instance_id
        # The description of the job template.
        self.app_description = app_description
        # The ID of the job template.
        self.app_id = app_id
        # The name of the job template.
        self.app_name = app_name
        # The maximum number of retries for a failed job.
        self.backoff_limit = backoff_limit
        # The Best-Effort policy.
        self.best_effort_type = best_effort_type
        # The image startup command. The command must be an executable that exists in the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # 
        # In this example, `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The arguments of the image startup command. The arguments are passed to the **Command** parameter. Format:
        # 
        # `["a","b"]`
        # 
        # In the example of the **Command** parameter, `CommandArgs=["abc", ">", "file0"]`. In this case, `["abc", ">", "file0"]` must be converted to a string in the format of a JSON array. If this parameter is not specified, you do not need to configure it.
        self.command_args = command_args
        # The concurrency policy for the job. Valid values:
        # 
        # - **Forbid**: Forbids concurrent runs. A new job is not created if the previous one has not completed.
        # 
        # - **Allow**: Allows concurrent runs.
        # 
        # - **Replace**: If the previous job has not completed, the new job replaces it.
        self.concurrency_policy = concurrency_policy
        # The information about the mounted ConfigMap.
        self.config_map_mount_desc = config_map_mount_desc
        # The number of CPU cores that are required by each instance. Unit: millicores. This parameter cannot be set to 0. Only the following fixed specifications are supported:
        # 
        # - **500**
        # 
        # - **1000**
        # 
        # - **2000**
        # 
        # - **4000**
        # 
        # - **8000**
        # 
        # - **16000**
        # 
        # - **32000**
        self.cpu = cpu
        # The custom host mapping in the container. The parameters are described as follows:
        # 
        # - **hostName**: The domain name or hostname.
        # 
        # - **ip**: The IP address.
        self.custom_host_alias = custom_host_alias
        # The version of the runtime environment in the HSF framework, such as an Ali-Tomcat container.
        self.edas_container_version = edas_container_version
        # The container environment variables. You can define custom variables or reference a ConfigMap. To reference a ConfigMap, you must first create a ConfigMap. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). The following formats are supported:
        # 
        # - Define custom variables
        # 
        #   - **name**: The name of the environment variable.
        # 
        #   - **value**: The value of the environment variable.
        # 
        # - Reference a ConfigMap
        # 
        #   - **name**: The name of the environment variable. You can reference a single key or all keys. To reference all keys, enter `sae-sys-configmap-all-<ConfigMap name>`, for example, `sae-sys-configmap-all-test1`.
        # 
        #   - **valueFrom**: The source of the environment variable. Set the value to `configMapRef`.
        # 
        #   - **configMapId**: The ID of the ConfigMap.
        # 
        #   - **key**: The key of the key-value pair. If you reference all keys in the ConfigMap, you do not need to specify this parameter.
        self.envs = envs
        # The ID of the Secret.
        self.image_pull_secrets = image_pull_secrets
        # The image URL. This parameter is required if **Package Type** is set to **Image**.
        self.image_url = image_url
        # The arguments for the startup of a JAR package. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_args = jar_start_args
        # The options for the startup of a JAR package. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_options = jar_start_options
        # The JDK version that the deployment package requires. The following versions are supported:
        # 
        # - **Open JDK 8**
        # 
        # - **Open JDK 7**
        # 
        # - **Dragonwell 11**
        # 
        # - **Dragonwell 8**
        # 
        # - **openjdk-8u191-jdk-alpine3.9**
        # 
        # - **openjdk-7u201-jdk-alpine3.9**
        # 
        # This parameter is not applicable if **Package Type** is set to **Image**.
        self.jdk = jdk
        # The memory required by each instance, in MB. This value cannot be 0. CPU and memory resources are allocated in fixed ratios. The following combinations are supported:
        # 
        # - **1024**: corresponds to 500 millicores and 1,000 millicores.
        # 
        # - **2048**: corresponds to 500, 1,000, and 2,000 millicores.
        # 
        # - **4096**: corresponds to 1,000, 2,000, and 4,000 millicores.
        # 
        # - **8192**: corresponds to 2,000, 4,000, and 8,000 millicores.
        # 
        # - **12288**: corresponds to 12,000 millicores.
        # 
        # - **16384**: corresponds to 4,000, 8,000, and 16,000 millicores.
        # 
        # - **24576**: corresponds to 12,000 millicores.
        # 
        # - **32768**: corresponds to 16,000 millicores.
        # 
        # - **65536**: corresponds to 8,000, 16,000, and 32,000 millicores.
        # 
        # - **131072**: corresponds to 32,000 millicores.
        self.memory = memory
        # The mount description.
        self.mount_desc = mount_desc
        # The mount target of the Apsara File Storage NAS file system in the job template\\"s VPC. You can omit this parameter if the NAS configuration is unchanged during redeployment. To clear the NAS configuration, set this parameter to an empty string (`""`).
        self.mount_host = mount_host
        # The namespace ID.
        self.namespace_id = namespace_id
        # The configuration for mounting an Apsara File Storage NAS file system.
        self.nas_configs = nas_configs
        # The ID of the Apsara File Storage NAS file system.
        self.nas_id = nas_id
        # The AccessKey ID for accessing Object Storage Service (OSS) buckets.
        self.oss_ak_id = oss_ak_id
        # The AccessKey secret for accessing OSS buckets.
        self.oss_ak_secret = oss_ak_secret
        # The description of the mounted OSS bucket.
        self.oss_mount_descs = oss_mount_descs
        # The type of the job package. Valid values:
        # 
        # - For Java deployments, **FatJar**, **War**, and **Image** are supported.
        # 
        # - For PHP deployments, the following package types are supported:
        # 
        #   - **PhpZip**
        # 
        #   - **IMAGE_PHP_5_4**
        # 
        #   - **IMAGE_PHP_5_4_ALPINE**
        # 
        #   - **IMAGE_PHP_5_5**
        # 
        #   - **IMAGE_PHP_5_5_ALPINE**
        # 
        #   - **IMAGE_PHP_5_6**
        # 
        #   - **IMAGE_PHP_5_6_ALPINE**
        # 
        #   - **IMAGE_PHP_7_0**
        # 
        #   - **IMAGE_PHP_7_0_ALPINE**
        # 
        #   - **IMAGE_PHP_7_1**
        # 
        #   - **IMAGE_PHP_7_1_ALPINE**
        # 
        #   - **IMAGE_PHP_7_2**
        # 
        #   - **IMAGE_PHP_7_2_ALPINE**
        # 
        #   - **IMAGE_PHP_7_3**
        # 
        #   - **IMAGE_PHP_7_3_ALPINE**
        # 
        # - For Python deployments, **PythonZip** and **Image** are supported.
        self.package_type = package_type
        # The URL of the package. This parameter is required if **Package Type** is set to **FatJar** or **War**.
        self.package_url = package_url
        # The version of the package. This parameter is required if **Package Type** is set to **FatJar** or **War**.
        self.package_version = package_version
        # The content of the PHP configuration file.
        self.php_config = php_config
        # The mount path of the PHP job startup configuration. Make sure that the PHP server uses this configuration to start.
        self.php_config_location = php_config_location
        # The script to execute after the container starts. This script runs immediately after the system creates the container. Example: `{"exec":{"command":["cat","/etc/group"]}}`
        self.post_start = post_start
        # The script to execute before the container stops. This script runs before the system deletes the container. Example: `{"exec":{"command":["cat","/etc/group"]}}`
        self.pre_stop = pre_stop
        # The programming language that is used for the job template. Valid values:
        # 
        # - **java**: Java
        # 
        # - **php**: PHP
        # 
        # - **python**: Python
        # 
        # - **other**: Other languages, such as C++, Go, .NET, and Node.js.
        self.programming_language = programming_language
        # The list of public request URLs for the one-time task.
        self.public_web_hook_urls = public_web_hook_urls
        # The Python environment. PYTHON 3.9.15 is supported.
        self.python = python
        # The Python module dependencies to install. By default, SAE installs dependencies from a `requirements.txt` file in the package\\"s root directory. Use this parameter to specify dependencies if a `requirements.txt` file is not present or to add extra modules.
        self.python_modules = python_modules
        # The ID of the referenced job template.
        self.ref_app_id = ref_app_id
        # The IDs of job templates that reference this template.
        self.refed_app_ids = refed_app_ids
        # The region ID.
        self.region_id = region_id
        # The number of job instances.
        self.replicas = replicas
        # The security group ID.
        self.security_group_id = security_group_id
        # Specifies whether to enable job sharding.
        self.slice = slice
        # The parameters for job sharding.
        self.slice_envs = slice_envs
        # The configuration for collecting logs to Log Service (SLS).
        # 
        # - Use an SLS resource that SAE automatically creates: `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # 
        # - Use a custom SLS resource: `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # The parameters are described as follows:
        # 
        # - **projectName**: The name of the SLS project.
        # 
        # - **logDir**: The log path.
        # 
        # - **logType**: The log type. **stdout** specifies the container\\"s standard output logs. You can specify only one log of the stdout type. If this parameter is omitted, file logs are collected.
        # 
        # - **logstoreName**: The name of the Logstore in SLS.
        # 
        # - **logtailName**: The name of the Logtail configuration in SLS. If you do not specify this parameter, a new Logtail configuration is created.
        # 
        # You can omit this parameter if the Log Service configuration is unchanged during redeployment. To disable log collection, set this parameter to an empty string (`""`).
        self.sls_configs = sls_configs
        # Specifies whether to suspend the job template.
        self.suspend = suspend
        # The tags of the job template.
        self.tags = tags
        # The timeout for a graceful stop, in seconds. Default: 30. Valid values: 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The timeout period for the job. Unit: seconds.
        self.timeout = timeout
        # The time zone. Default value: **Asia/Shanghai**.
        self.timezone = timezone
        # The Tomcat file configuration. To delete the configuration, set this parameter to "" or "{}".
        # 
        # - **port**: The port number. Valid values: 1024 to 65535. Ports below 1024 are reserved. If you do not specify a port, the default value is 8080.
        # 
        # - **contextPath**: The access path. Default value: /.
        # 
        # - **maxThreads**: The maximum number of connections in the connection pool. Default value: 400.
        # 
        # - **uriEncoding**: The URI encoding scheme for Tomcat. Valid values: **UTF-8**, **ISO-8859-1**, **GBK**, and **GB2312**. If you do not specify this parameter, the default value **ISO-8859-1** is used.
        # 
        # - **useBodyEncodingForUri**: Specifies whether to use the character encoding from the request body for the URI. Default value: **true**.
        self.tomcat_config = tomcat_config
        self.trigger_config = trigger_config
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The list of private request URLs for the one-time task.
        self.vpc_web_hook_urls = vpc_web_hook_urls
        # The options for the startup of a WAR package. The default startup command is `java $JAVA_OPTS $CATALINA_OPTS -Options org.apache.catalina.startup.Bootstrap "$@" start`.
        self.war_start_options = war_start_options
        # The version of the Tomcat container on which the package depends. The following versions are supported:
        # 
        # - **apache-tomcat-7.0.91**
        # 
        # - **apache-tomcat-8.5.42**
        # 
        # This parameter is not supported when **Package Type** is set to **Image**.
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
        # The bucket name.
        self.bucket_name = bucket_name
        # The directory or object that you created in the OSS bucket. An exception is returned if the specified mount directory does not exist.
        self.bucket_path = bucket_path
        # The path in your SAE container. If the path exists, it is overwritten. If the path does not exist, a new path is created.
        self.mount_path = mount_path
        # Specifies whether the container has read-only access to the mounted resources. Valid values:
        # 
        # - **true**: The path has read-only permissions.
        # 
        # - **false**: The path has read and write permissions.
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
        # The container mount path.
        self.mount_path = mount_path
        # The directory in the Apsara File Storage NAS file system.
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
        # The name of the ConfigMap.
        self.config_map_name = config_map_name
        # The key of the key-value pair in the ConfigMap.
        self.key = key
        # The container mount path.
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

