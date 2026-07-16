# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJobRequest(DaraModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_description: str = None,
        app_name: str = None,
        auto_config: bool = None,
        backoff_limit: int = None,
        best_effort_type: str = None,
        command: str = None,
        command_args: str = None,
        concurrency_policy: str = None,
        config_map_mount_desc: str = None,
        cpu: int = None,
        custom_host_alias: str = None,
        edas_container_version: str = None,
        enable_image_accl: bool = None,
        envs: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        memory: int = None,
        mount_desc: str = None,
        mount_host: str = None,
        namespace_id: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        programming_language: str = None,
        python: str = None,
        python_modules: str = None,
        ref_app_id: str = None,
        replicas: int = None,
        security_group_id: str = None,
        slice: bool = None,
        slice_envs: str = None,
        sls_configs: str = None,
        termination_grace_period_seconds: int = None,
        timeout: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        trigger_config: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
        workload: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is required to pull images across accounts. For more information, see [Grant permissions to pull images across Alibaba Cloud accounts by using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The ID of the Container Registry (ACR) Enterprise Edition instance. This parameter is required when **ImageUrl** points to an image in an ACR Enterprise Edition instance.
        self.acr_instance_id = acr_instance_id
        # The description of the job template. It cannot exceed 1,024 characters.
        self.app_description = app_description
        # The name of the job template. The name can contain letters, digits, and hyphens (-). It must start with a letter and be no longer than 36 characters.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Specifies whether to automatically configure the network environment. Valid values:
        # 
        # - **true**: SAE automatically configures the network environment when you create the job template. The values of **NamespaceId**, **VpcId**, **vSwitchId**, and **SecurityGroupId** are ignored.
        # 
        # - **false**: You must manually configure the network environment.
        self.auto_config = auto_config
        # The maximum number of retries for a task before it is marked as failed.
        self.backoff_limit = backoff_limit
        # The BestEffort policy.
        self.best_effort_type = best_effort_type
        # The entrypoint command for the container. The command must be an executable inside the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # 
        # For the preceding example, `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # Arguments for the entrypoint command (**Command**). The format is as follows:
        # 
        # `["a","b"]`
        # 
        # In the example for the `Command` parameter, the value for `CommandArgs` is `["abc", ">", "file0"]`. This value must be a string that contains a JSON array. If the command takes no arguments, you can omit this parameter.
        self.command_args = command_args
        # The concurrency policy for the task. Valid values:
        # 
        # - **Forbid**: Prohibits concurrent runs. A new task is not created if the previous one is not complete.
        # 
        # - **Allow**: Allows concurrent running.
        # 
        # - **Replace**: If a previous task is still running when the next one is scheduled, the new task replaces the old one.
        self.concurrency_policy = concurrency_policy
        # The **ConfigMap** mount description. Use a ConfigMap created in the namespace to inject configurations into the container. The parameters are described as follows:
        # 
        # - **configMapId**: The ID of the ConfigMap. You can call the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation to obtain this ID.
        # 
        # - **key**: The key.
        # 
        # > You can pass the `sae-sys-configmap-all` parameter to mount all keys.
        # 
        # - **mountPath**: The mount path in the container.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU required for each instance, in millicores. This value cannot be 0. Only the following fixed specifications are currently supported:
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
        # The host alias that maps a hostname to an IP address in the container. The parameters are described as follows:
        # 
        # - **hostName**: The domain name or hostname.
        # 
        # - **ip**: The IP address.
        self.custom_host_alias = custom_host_alias
        # The version of the HSF runtime environment for the task, such as an Ali-Tomcat container.
        self.edas_container_version = edas_container_version
        # Specifies whether to enable image acceleration. Valid values:
        # 
        # - **true**: Enables image acceleration.
        # 
        # - **false**: Disables image acceleration.
        self.enable_image_accl = enable_image_accl
        # Environment variables to set in the container. To reference variables, the ConfigMap must already exist. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). The value can be configured in one of the following ways:
        # 
        # - Specify custom variables
        # 
        #   - **name**: The name of the environment variable.
        # 
        #   - **value**: The value of the environment variable.
        # 
        # - Reference a ConfigMap
        # 
        #   - **name**: The name of the environment variable. You can reference a single key or all keys. To reference all keys, enter a value in the `sae-sys-configmap-all-<ConfigMap name>` format. Example: `sae-sys-configmap-all-test1`.
        # 
        #   - **valueFrom**: The source of the environment variable. Set the value to `configMapRef`.
        # 
        #   - **configMapId**: The ID of the ConfigMap.
        # 
        #   - **key**: The key to reference. If you want to reference all key-value pairs, do not specify this parameter.
        self.envs = envs
        # The ID of the secret used to pull the image.
        self.image_pull_secrets = image_pull_secrets
        # The URL of the image. This parameter is required when **PackageType** is set to **Image**.
        self.image_url = image_url
        # The startup arguments for the JAR package. The default startup command is: `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
        self.jar_start_args = jar_start_args
        # The startup options for the JAR package. The default startup command is: `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
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
        # This parameter is not supported when **PackageType** is set to **Image**.
        self.jdk = jdk
        # The memory required for each instance, in MB. This value cannot be 0. CPU and memory specifications are coupled. The following specifications are currently supported:
        # 
        # - **1024**: corresponds to 500 or 1,000 millicores of CPU.
        # 
        # - **2048**: corresponds to 500, 1,000, or 2,000 millicores of CPU.
        # 
        # - **4096**: corresponds to 1,000, 2,000, or 4,000 millicores of CPU.
        # 
        # - **8192**: corresponds to 2,000, 4,000, or 8,000 millicores of CPU.
        # 
        # - **12288**: corresponds to 12,000 millicores of CPU.
        # 
        # - **16384**: corresponds to 4,000, 8,000, or 16,000 millicores of CPU.
        # 
        # - **24576**: corresponds to 12,000 millicores of CPU.
        # 
        # - **32768**: corresponds to 16,000 millicores of CPU.
        # 
        # - **65536**: corresponds to 8,000, 16,000, or 32,000 millicores of CPU.
        # 
        # - **131072**: corresponds to 32,000 millicores of CPU.
        self.memory = memory
        # The NAS mount description. If this configuration does not change in subsequent deployments, you can omit this parameter. To clear the NAS configuration, set this parameter to an empty string ("").
        self.mount_desc = mount_desc
        # The NAS mount target in the VPC of the job template. If this configuration does not change in subsequent deployments, you can omit this parameter. To clear the NAS configuration, set this parameter to an empty string ("").
        self.mount_host = mount_host
        # The ID of the SAE namespace. The namespace name can contain only lowercase letters and hyphens (-), and must start with a letter.
        self.namespace_id = namespace_id
        # The configurations for mounting a NAS file system.
        self.nas_configs = nas_configs
        # The ID of the NAS file system. If this configuration does not change in subsequent deployments, you can omit this parameter. To clear the NAS configuration, set this parameter to an empty string ("").
        self.nas_id = nas_id
        # The AccessKey ID for reading from and writing to OSS.
        self.oss_ak_id = oss_ak_id
        # The AccessKey secret for reading from and writing to OSS.
        self.oss_ak_secret = oss_ak_secret
        # The description of the Object Storage Service (OSS) mount. The parameters are described as follows:
        # 
        # - **bucketName**: The name of the bucket.
        # 
        # - **bucketPath**: The directory or object in OSS. If the specified directory or object does not exist, an exception is thrown.
        # 
        # - **mountPath**: The path in the SAE container. If the path exists, it is overwritten. If the path does not exist, it is created.
        # 
        # - **readOnly**: Specifies whether the container has read-only access to the resources in the mount directory. Valid values:
        # 
        #   - **true**: read-only permission.
        # 
        #   - **false**: read and write permissions.
        self.oss_mount_descs = oss_mount_descs
        # The type of the deployment package. Valid values:
        # 
        # - For Java applications, valid values are **FatJar**, **War**, and **Image**.
        # 
        # - For PHP applications, the valid values are:
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
        # - For **Python** applications, valid values are **PythonZip** and **Image**.
        # 
        # This parameter is required.
        self.package_type = package_type
        # The URL of the deployment package. This parameter is required when **PackageType** is set to **FatJar**, **War**, or **PythonZip**.
        self.package_url = package_url
        # The version of the deployment package. This parameter is required when **PackageType** is set to **FatJar**, **War**, or **PythonZip**.
        self.package_version = package_version
        # The content of the PHP configuration file.
        self.php_config = php_config
        # The mount path of the startup configuration file for a PHP task. You must make sure that the PHP server uses this configuration file on startup.
        self.php_config_location = php_config_location
        # A PostStart hook. This script runs immediately after the container is created. The value must be a JSON string, for example: `{"exec":{"command":["sh","-c","echo hello"]}}`
        self.post_start = post_start
        # A PreStop hook. This script runs immediately before the container is stopped. The value must be a JSON string, for example: `{"exec":{"command":["sh","-c","echo hello"]}}`
        self.pre_stop = pre_stop
        # The programming language. Valid values: **java**, **php**, **python**, and **shell**.
        self.programming_language = programming_language
        # The Python environment. **PYTHON 3.9.15** is supported.
        self.python = python
        # Python dependencies to install by using pip. If you do not set this parameter, SAE installs dependencies from the \\"requirements.txt\\" file in the root directory of your project.
        self.python_modules = python_modules
        # The ID of the referenced job.
        self.ref_app_id = ref_app_id
        # The number of concurrent task instances.
        # 
        # This parameter is required.
        self.replicas = replicas
        # The security group ID.
        self.security_group_id = security_group_id
        # Specifies whether to enable task sharding.
        self.slice = slice
        # The parameters for task sharding.
        self.slice_envs = slice_envs
        # The configuration for collecting logs to Simple Log Service (SLS).
        # 
        # - To use SLS resources that are automatically created by SAE: `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # 
        # - To use your own SLS resources: `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # The parameters are described as follows:
        # 
        # - **projectName**: The name of the SLS Project.
        # 
        # - **logDir**: The path of the log file.
        # 
        # - **logType**: The log type. **stdout** indicates the standard output of the container. You can specify only one standard output. If you do not set this parameter, file logs are collected.
        # 
        # - **logstoreName**: The name of the Logstore in SLS.
        # 
        # - **logtailName**: The name of the Logtail in SLS. If you do not specify this parameter, a new Logtail is created.
        # 
        # If the log collection configuration does not change during subsequent deployments, you do not need to set this parameter (the request does not need to include the **SlsConfigs** field). If you no longer need to use the log collection feature, set the value of this parameter to an empty string ("") in your request.
        # 
        # > SAE deletes a project that it automatically created when you delete the corresponding job template. Therefore, if you specify an existing project, do not use one that was automatically created by SAE.
        self.sls_configs = sls_configs
        # The graceful shutdown timeout, in seconds. The value must be an integer from 1 to 300. Default: 30.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The task timeout, in seconds.
        self.timeout = timeout
        # The time zone. Default value: **Asia/Shanghai**.
        self.timezone = timezone
        # The Tomcat configuration. To delete the configuration, set this parameter to `""` or `{}`. The parameters are described as follows:
        # 
        # - **port**: The port number. The valid range is 1024 to 65535. Ports below 1024 require root permissions. Because the container is configured with administrator permissions, specify a port number greater than 1024. If this parameter is not configured, the default port 8080 is used.
        # 
        # - **contextPath**: The context path. Default value: /.
        # 
        # - **maxThreads**: The maximum number of threads in the connection pool. Default value: 400.
        # 
        # - **uriEncoding**: The URI encoding scheme for Tomcat. Valid values: **UTF-8**, **ISO-8859-1**, **GBK**, and **GB2312**. If this parameter is not set, the default value **ISO-8859-1** is used.
        # 
        # - **useBodyEncodingForUri**: Specifies whether to use the encoding specified in `request.getCharacterEncoding()` to decode the request URI. Default value: **true**.
        self.tomcat_config = tomcat_config
        self.trigger_config = trigger_config
        # The ID of the vSwitch for the elastic network interface of the task instance. The vSwitch must be located in the specified VPC. The vSwitch is also bound to the SAE namespace. If you do not specify this parameter, the ID of the vSwitch that is bound to the namespace is used by default.
        self.v_switch_id = v_switch_id
        # The ID of the VPC for the SAE namespace. In SAE, a namespace can be bound to only one VPC, and this binding cannot be changed. The binding is established when you create the first SAE job template in the namespace. A single VPC can be associated with multiple namespaces. If you do not specify this parameter, the ID of the VPC that is bound to the namespace is used by default.
        self.vpc_id = vpc_id
        # The startup command for a WAR package deployment. The configuration steps are the same as for an image-based deployment. For more information, see [Set a startup command](https://help.aliyun.com/document_detail/96677.html).
        self.war_start_options = war_start_options
        # The Tomcat version that the deployment package requires. The following versions are supported:
        # 
        # - **apache-tomcat-7.0.91**
        # 
        # - **apache-tomcat-8.5.42**
        # 
        # This parameter is not supported when **PackageType** is set to **Image**.
        self.web_container = web_container
        # The workload. Set the value to `job`.
        # 
        # This parameter is required.
        self.workload = workload

    def validate(self):
        pass

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

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config

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

        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.enable_image_accl is not None:
            result['EnableImageAccl'] = self.enable_image_accl

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

        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc

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

        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs

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

        if self.python is not None:
            result['Python'] = self.python

        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules

        if self.ref_app_id is not None:
            result['RefAppId'] = self.ref_app_id

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

        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        if self.workload is not None:
            result['Workload'] = self.workload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')

        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')

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

        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('EnableImageAccl') is not None:
            self.enable_image_accl = m.get('EnableImageAccl')

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

        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')

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

        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')

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

        if m.get('Python') is not None:
            self.python = m.get('Python')

        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')

        if m.get('RefAppId') is not None:
            self.ref_app_id = m.get('RefAppId')

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

        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        if m.get('Workload') is not None:
            self.workload = m.get('Workload')

        return self

