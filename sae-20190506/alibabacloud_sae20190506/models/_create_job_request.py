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
        # The Alibaba Cloud Resource Name (ARN) required for a RAM role to obtain images across accounts. For more information, see [Grant permissions across Alibaba Cloud accounts by using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The ID of Container Registry Enterprise Edition instance N. This parameter is required when the **ImageUrl** parameter is set to the URL of an image in an ACR Enterprise Edition instance.
        self.acr_instance_id = acr_instance_id
        # The description of the template. The description cannot exceed 1,024 characters in length.
        self.app_description = app_description
        # The name of the job template. The name can contain digits, letters, and hyphens (-). The name must start with a letter and cannot exceed 36 characters in length.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Specifies whether to automatically configure the network environment. Take note of the following rules:
        # 
        # *   **true**: The network environment is automatically configured by SAE when the application is created. In this case, the values of the **NamespaceId**, **VpcId**, **vSwitchId**, and **SecurityGroupId** parameters are ignored.
        # *   **false**: The network environment is manually configured based on your settings when the application is created.
        self.auto_config = auto_config
        # The number of times the job is retried.
        self.backoff_limit = backoff_limit
        self.best_effort_type = best_effort_type
        # The command that is used to start the image. The command must be an existing executable object in the container. Sample statements:
        # 
        #     command:
        #           - echo
        #           - abc
        #           - >
        #           - file0
        # 
        # In this example, the Command parameter is set to `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The parameters of the image startup command. The CommandArgs parameter specifies the parameters that are required for the **Command** parameter. You can specify the name in one of the following formats:
        # 
        # `["a","b"]`
        # 
        # In the preceding example, the CommandArgs parameter is set to `CommandArgs=["abc", ">", "file0"]`. The data type of `["abc", ">", "file0"]` must be an array of strings in the JSON format. This parameter is optional.
        self.command_args = command_args
        # The concurrency policy of the job. Take note of the following rules:
        # 
        # *   **Forbid**: Prohibits concurrent running. If the previous job is not completed, no new job is created.
        # *   **Allow**: Allows concurrent running.
        # *   **Replace**: If the previous job is not completed when the time to create a new job is reached, the new job replaces the previous job.
        self.concurrency_policy = concurrency_policy
        # The description of the **ConfigMap** instance mounted to the application. Use configurations created on the Configuration Items page to configure containers. The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **congfigMapId**: the ID of the ConfigMap instance. You can call the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation to obtain the ID.
        # *   **key**: the key.
        # 
        # > You can use the `sae-sys-configmap-all` key to mount all keys.
        # 
        # *   **mountPath**: the mount path in the container.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU specifications that are required for each instance. Unit: millicores. You cannot set this parameter to 0. Valid values:
        # 
        # *   500
        # *   1000
        # *   2000
        # *   4000
        # *   8000
        # *   16000
        # *   32000
        self.cpu = cpu
        # The custom mappings between hostnames and IP addresses in the container. Take note of the following rules:
        # 
        # *   **hostName**: the domain name or hostname.
        # *   **ip**: the IP address.
        self.custom_host_alias = custom_host_alias
        # The version of the container, such as Ali-Tomcat, in which an application developed based on High-speed Service Framework (HSF) is deployed.
        self.edas_container_version = edas_container_version
        self.enable_image_accl = enable_image_accl
        # The environment variables. You can configure custom environment variables or reference a ConfigMap. If you want to reference a ConfigMap, you must first create a ConfigMap. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Take note of the following rules:
        # 
        # *   Customize
        # 
        #     *   **name**: the name of the environment variable.
        #     *   **value**: the value of the environment variable.
        # 
        # *   Reference ConfigMap
        # 
        #     *   **name**: the name of the environment variable. You can reference one or all keys. If you want to reference all keys, specify `sae-sys-configmap-all-<ConfigMap name>`. Example: `sae-sys-configmap-all-test1`.
        #     *   **valueFrom**: the reference of the environment variable. Set the value to `configMapRef`.
        #     *   **configMapId**: the ConfigMap ID.
        #     *   **key**: the key. If you want to reference all keys, do not configure this parameter.
        self.envs = envs
        # The ID of the corresponding Secret.
        self.image_pull_secrets = image_pull_secrets
        # The URL of the image. This parameter is returned only if the **PackageType** parameter is set to **Image**.
        self.image_url = image_url
        # The arguments in the JAR package. The arguments are used to start the application container. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_args = jar_start_args
        # The option settings in the JAR package. The settings are used to start the application container. The default startup command for application deployment is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_options = jar_start_options
        # The version of the Java development kit (JDK) on which the deployment package of the application depends. The following versions are supported:
        # 
        # *   **Open JDK 8**
        # *   **Open JDK 7**
        # *   **Dragonwell 11**
        # *   **Dragonwell 8**
        # *   **openjdk-8u191-jdk-alpine3.9**
        # *   **openjdk-7u201-jdk-alpine3.9**
        # 
        # This parameter is not returned if the **PackageType** parameter is set to **Image**.
        self.jdk = jdk
        # The size of memory required by each instance. Unit: MB. You cannot set this parameter to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   Set the value to 1024 when Cpu is set to 500 or 1000.
        # *   Set the value to 2048 when Cpu is set to 500, 1000 or 2000.
        # *   Set the value to 4096 when Cpu is set to 1000, 2000, or 4000.
        # *   Set the value to 8192 when Cpu is set to 2000, 4000, or 8000.
        # *   Set the value to 12288 when Cpu is set to 12000.
        # *   Set the value to 16384 when Cpu is set to 4000, 8000, or 16000.
        # *   Set the value to 24576 when Cpu is set to 12000.
        # *   Set the value to 32768 when Cpu is set to 16000.
        # *   Set the value to 65536 when Cpu is set to 8000, 16000, or 32000.
        # *   Set the value to 131072 when Cpu is set to 32000.
        self.memory = memory
        # The configurations for mounting the NAS file system. After the application is created, you may want to call other operations to manage the application. If you do not want to change the NAS configurations in these subsequent operations, you can omit the **MountDesc** parameter in the requests. If you want to unmount the NAS file system, you must set the **MountDesc** values in the subsequent requests to an empty string ("").
        self.mount_desc = mount_desc
        # The mount target of the NAS file system in the VPC where the application is deployed. If you do not need to modify this configuration during the deployment, configure the **MountHost** parameter only in the first request. You do not need to include this parameter in subsequent requests. If you need to remove this configuration, leave the **MountHost** parameter empty in the request.
        self.mount_host = mount_host
        # The ID of the Serverless App Engine (SAE) namespace. The ID can contain only lowercase letters and hyphens (-). It must start with a lowercase letter.
        self.namespace_id = namespace_id
        self.nas_configs = nas_configs
        # The ID of the Apsara File Storage NAS file system. After the application is created, you may want to call other operations to manage the application. If you do not want to change the NAS configurations in these subsequent operations, you can omit the **NasId** parameter in the requests. If you want to unmount the NAS file system, you must set the **NasId** values in the subsequent requests to an empty string ("").
        self.nas_id = nas_id
        # The AccessKey ID that is used to read data from and write data to Object Storage Service (OSS) buckets.
        self.oss_ak_id = oss_ak_id
        # The AccessKey secret that is used to read data from and write data to OSS buckets.
        self.oss_ak_secret = oss_ak_secret
        # Information of the Object Storage Service (OSS) bucket mounted to the application. The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **bucketName**: the name of the OSS bucket.
        # 
        # *   **bucketPath**: the directory or object in OSS. If the specified directory or object does not exist, an error is returned.
        # 
        # *   **mountPath**: the directory of the container in SAE. If the path already exists, the newly specified path overwrites the previous one. If the path does not exist, it is created.
        # 
        # *   **readOnly**: specifies whether to only allow the container path to read data from the OSS directory. Valid values:
        # 
        #     *   **true**: The container path only has read permission on the OSS directory.
        #     *   **false**: The application has read and write permissions.
        self.oss_mount_descs = oss_mount_descs
        # The type of the deployment package. Take note of the following rules:
        # 
        # *   If you deploy the application by using a Java Archive (JAR) package, you can set this parameter to **FatJar**, **War**, or **Image**.
        # *   If you deploy the application by using a PHP package, you can set this parameter to one of the following values:
        # 
        # **PhpZip** **IMAGE_PHP_5_4** **IMAGE_PHP_5_4_ALPINE** **IMAGE_PHP_5_5** **IMAGE_PHP_5_5_ALPINE** **IMAGE_PHP_5_6** **IMAGE_PHP_5_6_ALPINE** **IMAGE_PHP_7_0** **IMAGE_PHP_7_0_ALPINE** **IMAGE_PHP_7_1** **IMAGE_PHP_7_1_ALPINE** **IMAGE_PHP_7_2** **IMAGE_PHP_7_2_ALPINE** **IMAGE_PHP_7_3** **IMAGE_PHP_7_3_ALPINE**
        # 
        # *   If you deploy the application by using a **Python** package, you can set this parameter to **PythonZip** or **Image**:
        # 
        # This parameter is required.
        self.package_type = package_type
        # The address of the deployment package. This parameter is required if you set **PackageType** to **FatJar**, **War**, or **PythonZip**.
        self.package_url = package_url
        # The version of the deployment package. This parameter is required if you set **PackageType** to **FatJar**, **War**, or **PythonZip**.
        self.package_version = package_version
        # The details of the PHP configuration file.
        self.php_config = php_config
        # The path on which the PHP configuration file for application startup is mounted. Make sure that the PHP server uses this configuration file during the startup.
        self.php_config_location = php_config_location
        # The script that is run immediately after the container is started. Example: `{"exec":{"command":["sh","-c","echo hello"\\]}}`
        self.post_start = post_start
        # The script that is run before the container is stopped. Example: `{"exec":{"command":["sh","-c","echo hello"\\]}}`
        self.pre_stop = pre_stop
        # The programming language. Valid values: **java**, **php**, **python**, and **shell**.
        self.programming_language = programming_language
        # The Python environment. Set the value to **PYTHON 3.9.15**.
        self.python = python
        # The configurations for installing custom module dependencies. By default, the dependencies defined by the requirements.txt file in the root directory are installed. If the package does not contain this file and you do not configure custom dependencies in the package, specify the dependencies that you want to install in the text box.
        self.python_modules = python_modules
        # The ID of the job that you reference.
        self.ref_app_id = ref_app_id
        # The number of concurrent instances.
        # 
        # This parameter is required.
        self.replicas = replicas
        # The ID of the security group.
        self.security_group_id = security_group_id
        # Specifies whether to enable job sharding.
        self.slice = slice
        # The parameters of job sharding.
        self.slice_envs = slice_envs
        # The logging configurations of Log Service.
        # 
        # *   To use Log Service resources that are automatically created by SAE, set this parameter to `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # *   To use custom Log Service resources, set this parameter to `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **projectName**: the name of the Log Service project.
        # *   **logDir**: the path in which logs are stored.
        # *   **logType**: the log type. **stdout**: the standard output log of the container. You can specify only one stdout value for this parameter. If you leave this parameter empty, file logs are collected.
        # *   **logstoreName**: the name of the Logstore in Log Service.
        # *   **logtailName**: the name of the Logtail configuration in Log Service. If you do not configure this parameter, a new Logtail configuration is created.
        # 
        # If you do not need to modify the logging configurations when you deploy the application, configure the **SlsConfigs** parameter only in the first request. You do not need to include this parameter in subsequent requests. If you no longer need to use Log Service, leave the **SlsConfigs** parameter empty in the request.
        # 
        # > A Log Service project that is automatically created by SAE when you create an application is deleted when the application is deleted. Therefore, when you create an application, you cannot select a Log Service project that is automatically created by SAE for log collection.
        self.sls_configs = sls_configs
        # The timeout period for a graceful shutdown. Default value: 30. Unit: seconds. Valid values: 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The timeout period. Unit: seconds.
        self.timeout = timeout
        # The time zone. Default value: **Asia/Shanghai**.
        self.timezone = timezone
        # The Tomcat configuration. If you want to cancel this configuration, set this parameter to "" or "{}". The following variables are included in the configuration: Take note of the following rules:
        # 
        # *   **port**: the port number. The port number ranges from 1024 to 65535. Though the admin permissions are configured for the container, the root permissions are required to perform operations on ports whose number is smaller than 1024. Enter a value that ranges from 1025 to 65535 because the container has only the admin permissions. If you do not specify this parameter, the default port number 8080 is used.
        # *   **contextPath**: the path. Default value: /. This value indicates the root directory.
        # *   **maxThreads**: the maximum number of connections in the connection pool. Default value: 400.
        # *   **uriEncoding**: the URI encoding scheme in the Tomcat container. Valid values: UTF-8, ISO-8859-1, GBK, and GB2312.************ If you do not specify this parameter, the default value **ISO-8859-1** is used.
        # *   **useBodyEncoding**: specifies whether to use the encoding scheme specified in the request body for URI query parameters. Default value: true.
        self.tomcat_config = tomcat_config
        self.trigger_config = trigger_config
        # The vSwitch to which the elastic network interface (ENI) of the application instance is connected. The vSwitch must be located in the VPC specified by the VpcId parameter. The SAE namespace is bound with this vSwitch. The default value is the ID of the vSwitch that is bound to the namespace.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) that corresponds to the SAE namespace. In SAE, once correspondence is configured between a namespace and a VPC, the namespace cannot correspond to other VPCs. When the SAE application is created within the namespace, the application is bound with the VPC. Multiple namespaces can correspond to the same VPC. The default value is the ID of the VPC that is bound to the namespace.
        self.vpc_id = vpc_id
        # The startup command of the WAR package. For information about how to configure the startup command, see [Configure startup commands](https://help.aliyun.com/document_detail/96677.html).
        self.war_start_options = war_start_options
        # The version of the Tomcat container on which the deployment package depends. Valid values:
        # 
        # *   **apache-tomcat-7.0.91**
        # *   **apache-tomcat-8.5.42**
        # 
        # This parameter is not returned if the **PackageType** parameter is set to **Image**.
        self.web_container = web_container
        # Set the value to `job`.
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

