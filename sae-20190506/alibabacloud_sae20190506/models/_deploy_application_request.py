# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DeployApplicationRequest(DaraModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        agent_version: str = None,
        alb_ingress_readiness_gate: str = None,
        app_id: str = None,
        associate_eip: bool = None,
        auto_enable_application_scaling_rule: bool = None,
        batch_wait_time: int = None,
        change_order_desc: str = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        cpu: int = None,
        custom_host_alias: str = None,
        custom_image_network_type: str = None,
        deploy: str = None,
        dotnet: str = None,
        edas_container_version: str = None,
        empty_dir_desc: str = None,
        enable_ahas: str = None,
        enable_cpu_burst: bool = None,
        enable_grey_tag_route: bool = None,
        enable_namespace_agent_version: bool = None,
        enable_new_arms: bool = None,
        enable_prometheus: bool = None,
        enable_sidecar_resource_isolated: bool = None,
        envs: str = None,
        gpu_config: str = None,
        html: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        init_containers_config: List[main_models.InitContainerConfig] = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        kafka_configs: str = None,
        liveness: str = None,
        loki_configs: str = None,
        max_surge_instance_ratio: int = None,
        max_surge_instances: int = None,
        memory: int = None,
        micro_registration: str = None,
        micro_registration_config: str = None,
        microservice_engine_config: str = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        mount_desc: str = None,
        mount_host: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        new_sae_version: str = None,
        oidc_role_name: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        pvtz_discovery_svc: str = None,
        python: str = None,
        python_modules: str = None,
        readiness: str = None,
        replicas: int = None,
        secret_mount_desc: str = None,
        security_group_id: str = None,
        service_tags: str = None,
        sidecar_containers_config: List[main_models.SidecarContainerConfig] = None,
        sls_configs: str = None,
        sls_log_env_tags: str = None,
        startup_probe: str = None,
        swimlane_pvtz_discovery_svc: str = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        update_strategy: str = None,
        v_switch_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) required for a RAM role to obtain images across accounts. For more information, see [Grant permissions across Alibaba Cloud accounts by using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The ID of Container Registry Enterprise Edition instance N. This parameter is required when the **ImageUrl** parameter is set to the URL of an image in an ACR Enterprise Edition instance.
        self.acr_instance_id = acr_instance_id
        self.agent_version = agent_version
        self.alb_ingress_readiness_gate = alb_ingress_readiness_gate
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to associate an EIP with the node pool. Take note of the following rules:
        # 
        # *   **true**: The EIP is associated with the application instance.
        # *   **false**: The EIP is not associated with the application instance.
        self.associate_eip = associate_eip
        # Specifies whether to automatically enable an auto scaling policy for the application. Take note of the following rules:
        # 
        # *   **true**: turns on Logon-free Sharing
        # *   **false**: turns off Logon-free Sharing
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        # The interval between batches during a batch release. Unit: minutes.
        self.batch_wait_time = batch_wait_time
        # The description of the change order.
        self.change_order_desc = change_order_desc
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
        # The description of the **ConfigMap** instance mounted to the application. Use configurations created on the Configuration Items page to configure containers. The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **congfigMapId**: the ID of the ConfigMap instance. You can call the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation to obtain the ID.
        # *   **key**: the key.
        # 
        # > You can use `sae-sys-configmap-all` to mount all keys.
        # 
        # *   **mountPath**: the mount path in the container.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU specifications that are required for each instance. Unit: millicores. This parameter cannot be set to 0. Valid values:
        # 
        # *   **500**
        # *   **1000**
        # *   **2000**
        # *   **4000**
        # *   **8000**
        # *   **12000**
        # *   **16000**
        # *   **32000**
        self.cpu = cpu
        # The custom mappings between hostnames and IP addresses in the container. Take note of the following rules:
        # 
        # *   **hostName**: the domain name or hostname.
        # *   **ip**: the IP address.
        self.custom_host_alias = custom_host_alias
        # Custom image type. To it to empty string to use pre-built image.
        # 
        # - internet: Public network image
        # 
        # - intranet: Private network image
        self.custom_image_network_type = custom_image_network_type
        # This parameter takes effect only for applications that are in the Stopped state. If you call the **DeployApplication** operation to manage a running application, the application is immediately redeployed.
        # 
        # *   **true** (default): specifies that the system immediately deploys the application, enables new configurations, and pulls application instances.
        # *   **false**: specifies that the system only enables the new configurations.
        self.deploy = deploy
        # The version of .NET
        # 
        # - .NET 3.1
        # - .NET 5.0
        # - .NET 6.0
        # - .NET 7.0
        # - .NET 8.0
        self.dotnet = dotnet
        # The version of the container, such as Ali-Tomcat, in which an application developed based on High-speed Service Framework (HSF) is deployed.
        self.edas_container_version = edas_container_version
        self.empty_dir_desc = empty_dir_desc
        # Indicates whether access to Application High Availability Service (AHAS) is enabled. Take note of the following rules:
        # 
        # *   **true**: Access to AHAS is enabled.
        # *   **false**: Access to AHAS is disabled.
        self.enable_ahas = enable_ahas
        # Enable CPU Burst.
        # 
        # true: enable
        # 
        # false: disable
        self.enable_cpu_burst = enable_cpu_burst
        # Indicates whether canary release rules are enabled. Canary release rules apply only to applications in Spring Cloud and Dubbo frameworks. Take note of the following rules:
        # 
        # *   **true**: The canary release rules are enabled.
        # *   **false**: The canary release rules are disabled.
        self.enable_grey_tag_route = enable_grey_tag_route
        self.enable_namespace_agent_version = enable_namespace_agent_version
        # Enable new ARMS features.
        # 
        # - true: enable
        # 
        # - false: disable
        self.enable_new_arms = enable_new_arms
        self.enable_prometheus = enable_prometheus
        # Enable Sidecar resource isolation.
        # 
        # true: enable
        # 
        # false: disable
        self.enable_sidecar_resource_isolated = enable_sidecar_resource_isolated
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
        # 
        # *   Reference secret dictionary
        # 
        #     *   **name**: the name of the environment variable. You can reference one or all keys. If you want to reference all keys, specify `sae-sys-secret-all-<Secret dictionary name>`. Example: `sae-sys-secret-all-test1`.
        #     *   **valueFrom**: the reference of the environment variable. Set the value to `secretRef`.
        #     *   **secretId**: the secret dictionary ID.
        #     *   **key**: the key. If you want to reference all keys, do not configure this parameter.
        self.envs = envs
        self.gpu_config = gpu_config
        self.html = html
        # The ID of the corresponding Secret.
        self.image_pull_secrets = image_pull_secrets
        # The URL of the image. This parameter is returned only if the **PackageType** parameter is set to **Image**.
        self.image_url = image_url
        # Initialize container configuration.
        self.init_containers_config = init_containers_config
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
        # The logging configurations of Message Queue for Apache Kafka. Take note of the following rules:
        # 
        # *   **kafkaEndpoint**: the endpoint of the Message Queue for Apache Kafka API.
        # *   **kafkaInstanceId**: the ID of the Message Queue for Apache Kafka instance.
        # *   **kafkaConfigs**: One or more logging configurations of Message Queue for Apache Kafka. For information about sample values and parameters, see the request parameter **KafkaLogfileConfig** in this topic.
        self.kafka_configs = kafka_configs
        # The details of the availability check that was performed on the container. If the container fails this health check multiple times, the system disables and restarts the container. You can use one of the following methods to perform the health check:
        # 
        # *   Example of **exec**: `{"exec":{"command":["sh","-c","cat/home/admin/start.sh"]},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":2}`
        # *   Sample code of the **httpGet** method: `{"httpGet":{"path":"/","port":18091,"scheme":"HTTP","isContainKeyWord":true,"keyWord":"SAE"},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # *   Sample code of the **tcpSocket** method: `{"tcpSocket":{"port":18091},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # > You can use only one method to perform the health check.
        # 
        # The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **exec.command**: the health check command.
        # *   **httpGet.path**: the request path.
        # *   **httpGet.scheme**: the protocol that is used to perform the health check. Valid values: **HTTP** and **HTTPS**.
        # *   **httpGet.isContainKeyWord**: indicates whether the response contains keywords. Valid values: **true** and **false**. If this field is not returned, the advanced settings are not used.
        # *   **httpGet.keyWord**: the custom keyword. This parameter is available only if the **isContainKeyWord** field is returned.
        # *   **tcpSocket.port**: the port that is used to check the status of TCP connections.
        # *   **initialDelaySeconds**: the delay of the health check. Default value: 10. Unit: seconds.
        # *   **periodSeconds**: the interval at which health checks are performed. Default value: 30. Unit: seconds.
        # *   **timeoutSeconds**: the timeout period of the health check. Default value: 1. Unit: seconds. If you set this parameter to 0 or leave this parameter empty, the timeout period is automatically set to 1 second.
        self.liveness = liveness
        self.loki_configs = loki_configs
        self.max_surge_instance_ratio = max_surge_instance_ratio
        self.max_surge_instances = max_surge_instances
        # The memory size that is required by each instance. Unit: MB. This parameter cannot be set to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   This parameter is set to **1024** if the Cpu parameter is set to 500 or 1000.
        # *   This parameter is set to **2048** if the Cpu parameter is set to 500, 1000, or 2000.
        # *   This parameter is set to **4096** if the Cpu parameter is set to 1000, 2000, or 4000.
        # *   This parameter is set to **8192** if the Cpu parameter is set to 2000, 4000, or 8,000.
        # *   This parameter is set to **12288** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **16384** if the Cpu parameter is set to 4000, 8000, or 16000.
        # *   This parameter is set to **24576** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **32768** if the Cpu parameter is set to 16000.
        # *   This parameter is set to **65536** if the Cpu parameter is set to 8000, 16000, or 32000.
        # *   This parameter is set to **131072** if the Cpu parameter is set to 32000.
        self.memory = memory
        # The Nacos registry. Valid values:
        # 
        # *   **0**: SAE built-in Nacos registry
        # *   **1**: self-managed Nacos registry
        # *   **2** : MSE Nacos registry
        self.micro_registration = micro_registration
        # Select the edition of Nacos.
        # 
        # - 0: SAE built-in Nacos. Unable to get the configuration of SAE built-in Nacos.
        # 
        # - 1: Self-built Nacos from users.
        # 
        # - 2: MSE enterprise Nacos.
        self.micro_registration_config = micro_registration_config
        # Configure Microservices Governance
        # 
        # Whether to enable microservices governance (enable):
        # - true: Enable
        # - false: Disable
        # 
        # Configure lossless online/offline deployment (mseLosslessRule):
        # 
        # delayTime: Delay duration (unit: seconds)
        # 
        # enable: Whether to enable lossless deployment
        # 
        # - true: Enable
        # 
        # - false: Disable
        # 
        # notice: Whether to enable notifications
        # 
        # - true: Enable
        # 
        # - false: Disable
        # 
        # warmupTime: Small-traffic warm-up duration (unit: seconds)
        self.microservice_engine_config = microservice_engine_config
        # The percentage of the minimum number of available instances. Take note of the following rules:
        # 
        # *   If you set the value to **-1**, the minimum number of available instances is not determined based on this parameter. Default value: -1.
        # *   If you set the value to a number **from 0 to 100**, the minimum number of available instances is calculated by using the following formula: Current number of instances × (Value of MinReadyInstanceRatio × 100%). The value is the nearest integer rounded up from the calculated result. For example, if the percentage is set to **50**% and five instances are available, the minimum number of available instances is 3.
        # 
        # > When both **MinReadyInstance** and **MinReadyInstanceRatio** are specified and **MinReadyInstanceRatio** is set to a number from 0 to 100, the value of **MinReadyInstanceRatio**** takes precedence. For example, if **MinReadyInstances** is set to **5, and **MinReadyInstanceRatio** is set to **50**, the minimum number of available instances is set to the nearest integer rounded up from the calculated result of the following formula: Current number of instances × **50%**.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of available instances. Special values:
        # 
        # *   If you set the value to **0**, business interruptions occur when the application is updated.
        # *   If you set the value to \\*\\*-1\\*\\*, the minimum number of available instances is automatically set to a system-recommended value. The value is the nearest integer to which the calculated result of the following formula is rounded up: Current number of instances × 25%. For example, if five instances are available, the minimum number of available instances is calculated by using the following formula: 5 × 25% = 1.25. In this case, the minimum number of available instances is 2.
        # 
        # > Make sure that at least one instance is available during application deployment and rollback to prevent business interruptions.
        self.min_ready_instances = min_ready_instances
        # The configurations for mounting the NAS file system. After the application is created, you may want to call other operations to manage the application. If you do not want to change the NAS configurations in these subsequent operations, you can omit the **MountDesc** parameter in the requests. If you want to unmount the NAS file system, you must set the **MountDesc** values in the subsequent requests to an empty string ("").
        self.mount_desc = mount_desc
        # The mount target of the NAS file system in the VPC where the application is deployed. If you do not need to modify this configuration during the deployment, configure the **MountHost** parameter only in the first request. You do not need to include this parameter in subsequent requests. If you need to remove this configuration, leave the **MountHost** parameter empty in the request.
        self.mount_host = mount_host
        # The configurations of mounting the NAS file system. Take note of the following rules:
        # 
        # *   **mountPath**: the mount path of the container.
        # *   **readOnly**: If you set the value to **false**, the application has the read and write permissions.
        # *   **nasId**: the ID of the NAS file system.
        # *   **mountDomain**: the domain name of the mount target. For more information, see [DescribeMountTargets](https://help.aliyun.com/document_detail/62626.html).
        # *   **nasPath**: the directory in the NAS file system.
        self.nas_configs = nas_configs
        # The ID of the File Storage NAS file system. After the application is created, you may want to call other operations to manage the application. If you do not want to change the NAS configurations in these subsequent operations, you can omit the **NasId** parameter in the requests. If you want to unmount the NAS file system, you must set the **NasId** values in the subsequent requests to an empty string ("").
        self.nas_id = nas_id
        # SAE edition.
        # 
        # - lite: the lightweight edition.
        # 
        # - std: the standard edition.
        # 
        # - pro: the professional edition.
        self.new_sae_version = new_sae_version
        # The name of the RAM role used to authenticate the user identity.
        # 
        # >  You need to create an OpenID Connect (OIDC) identity provider (IdP) and an identity provider (IdP) for role-based single sign-on (SSO) in advance. For more information, see [Creates an OpenID Connect (OIDC) identity provider (IdP)](https://help.aliyun.com/document_detail/2331022.html) and [Creates an identity provider (IdP) for role-based single sign-on (SSO)](https://help.aliyun.com/document_detail/2331016.html).
        self.oidc_role_name = oidc_role_name
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
        # The package type.
        # 
        # When using Java, FatJar, War and Image are supported.
        # When using Python, PythonZip and Image are supported.
        # When using PHP, the followings are supported:
        # - PhpZip
        # - IMAGE_PHP_5_4
        # - IMAGE_PHP_5_4_ALPINE
        # - IMAGE_PHP_5_5
        # - IMAGE_PHP_5_5_ALPINE
        # - IMAGE_PHP_5_6
        # - IMAGE_PHP_5_6_ALPINE
        # - IMAGE_PHP_7_0
        # - IMAGE_PHP_7_0_ALPINE
        # - IMAGE_PHP_7_1
        # - IMAGE_PHP_7_1_ALPINE
        # - IMAGE_PHP_7_2
        # - IMAGE_PHP_7_2_ALPINE
        # - IMAGE_PHP_7_3
        # - IMAGE_PHP_7_3_ALPINE
        self.package_type = package_type
        # The address of the deployment package. This parameter is required when the **PackageType** parameter is set to **FatJar**, **War**, or **PythonZip**.
        self.package_url = package_url
        # The version of the deployment package. This parameter is required when the **PackageType** parameter is set to **FatJar**, **War**, or **PythonZip**.
        self.package_version = package_version
        # The dependent PHP version of PHP package. Image is not supported.
        self.php = php
        # The path on which the PHP configuration file for application monitoring is mounted. Make sure that the PHP server loads the configuration file. SAE automatically generates the corresponding configuration file. No manual operations are required.
        self.php_arms_config_location = php_arms_config_location
        # The details of the PHP configuration file.
        self.php_config = php_config
        # The path on which the PHP configuration file for application startup is mounted. Make sure that the PHP server uses this configuration file during the startup.
        self.php_config_location = php_config_location
        # The script that is run immediately after the container is started. Example: `{"exec":{"command":["sh","-c","echo hello"\\]}}`
        self.post_start = post_start
        # The script that is run before the container is stopped. Example: `{"exec":{"command":["sh","-c","echo hello"\\]}}`
        self.pre_stop = pre_stop
        # The configurations of Kubernetes Service-based service registration and discovery. Take note of the following rules:
        # 
        # *   **serviceName**: the name of the Alibaba Cloud service. Format: `<Custom content>-<Namespace ID>`. `-<Namespace ID>` is automatically specified based on the namespace in which an application resides and cannot be changed. For example, if you select the default namespace in the China (Beijing) region, `-cn-beijing-default` is automatically specified.
        # *   **namespaceId**: the namespace ID.
        # *   **portAndProtocol**: the port number and protocol. Valid values of the port number: 1 to 65535. Valid values of the protocol: **TCP** and **UDP**.
        # *   **enable**: enables the Kubernetes Service-based registration and discovery feature.
        self.pvtz_discovery_svc = pvtz_discovery_svc
        # The Python environment. Set the value to **PYTHON 3.9.15**.
        self.python = python
        # The configurations for installing custom module dependencies. By default, the dependencies defined by the requirements.txt file in the root directory are installed. If the package does not contain this file and you do not configure custom dependencies in the package, specify the dependencies that you want to install in the text box.
        self.python_modules = python_modules
        # The details of the health check that was performed on the container. If the container fails this health check multiple times, the system disables and restarts the container. Containers that fail health checks cannot receive traffic from Server Load Balancer (SLB) instances. You can use the **exec**, **httpGet**, or **tcpSocket** method to perform health checks. For more information, see the description of the **Liveness** parameter.
        # 
        # > You can use only one method to perform the health check.
        self.readiness = readiness
        # The number of instances.
        self.replicas = replicas
        # Secret Mount Description
        # Use the secret dictionaries created in the Namespace Secret Dictionary page to inject information into containers. Parameter descriptions are as follows:
        # 
        # - secretId: Secret instance ID. Obtain via the ListSecrets interface.
        # 
        # - key: Key-value pair. Note: Set the parameter sae-sys-secret-all to mount all keys.
        # 
        # - mountPath: Mount path.
        self.secret_mount_desc = secret_mount_desc
        # Security group ID.
        self.security_group_id = security_group_id
        # The gray-release tag of the application.
        self.service_tags = service_tags
        # The configuration of the container.
        self.sidecar_containers_config = sidecar_containers_config
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
        self.sls_log_env_tags = sls_log_env_tags
        # Check Failure: Indicates that the application failed to start. The system will report the exception and automatically restart it.
        # 
        # Note: 
        # 
        # Supports exec, httpGet, and tcpSocket methods. For specific examples, see Liveness Parameters.
        # Only one method can be selected for health checks.
        self.startup_probe = startup_probe
        # Configure K8s Service-based Service Registration/Discovery and Full-Chain Grayscale Capabilities
        # 
        # - enable: Whether to enable full-link grayscale based on K8s Service (set to "true" to enable; set to "false" to disable).
        # 
        # - namespaceId: Namespace ID
        # 
        # - portAndProtocol: Listener port and protocol. Format: {"Port:Protocol Type":"Container Port"}
        # - portProtocols: Define service ports and protocols
        # port: Port
        # protocol: Protocol
        # targetPort: Container port
        # 
        # - pvtzDiscoveryName: Service discovery name
        # 
        # - serviceId: Service ID
        # 
        # - serviceName: Service name
        self.swimlane_pvtz_discovery_svc = swimlane_pvtz_discovery_svc
        # The timeout period for a graceful shutdown. Default value: 30. Unit: seconds. Valid values: 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
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
        # The deployment policy. If the minimum number of available instances is 1, the value of the **UpdateStrategy** parameter is an empty string (""). If the minimum number of available instances is greater than 1, the following strategies can be configured:
        # 
        # *   The application is deployed on an instance. The remaining instances are automatically classified into two release batches whose interval is set to 1. In this case, the parameter is set to `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":1},"grayUpdate":{"gray":1}}`.
        # *   The application is deployed on an instance. The remaining instances are manually classified into two release batches. In this case, the parameter is set to `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"manual"},"grayUpdate":{"gray":1}}`.
        # *   All instances are automatically classified into two release batches. The application is deployed on the instances of the two batches in parallel. In this case, the parameter is set to `{"type":"BatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":0}}`
        # 
        # The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **type**: the type of the release policy. Valid values: **GrayBatchUpdate** and **BatchUpdate**.
        # 
        # *   **batchUpdate**: the phased release policy.
        # 
        #     *   **batch**: the number of release batches.
        #     *   **releaseType**: the processing method for the batches. Valid values: **auto** and **manual**.
        #     *   **batchWaitTime**: the interval between release batches. Unit: seconds.
        # 
        # *   **grayUpdate**: the number of release batches in the phased release after a canary release. This parameter is returned only if the **type** parameter is set to **GrayBatchUpdate**.
        self.update_strategy = update_strategy
        # The ID of the vSwitch, where the EIP of the application instances resides. The vSwitch must reside in the VPC above.
        self.v_switch_id = v_switch_id
        # The startup command of the WAR package. For information about how to configure the startup command, see [Configure startup commands](https://help.aliyun.com/document_detail/96677.html).
        self.war_start_options = war_start_options
        # The version of the Tomcat container on which the deployment package depends. Valid values:
        # 
        # *   **apache-tomcat-7.0.91**
        # *   **apache-tomcat-8.5.42**
        # 
        # This parameter is not returned if the **PackageType** parameter is set to **Image**.
        self.web_container = web_container

    def validate(self):
        if self.init_containers_config:
            for v1 in self.init_containers_config:
                 if v1:
                    v1.validate()
        if self.sidecar_containers_config:
            for v1 in self.sidecar_containers_config:
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

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.alb_ingress_readiness_gate is not None:
            result['AlbIngressReadinessGate'] = self.alb_ingress_readiness_gate

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip

        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule

        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time

        if self.change_order_desc is not None:
            result['ChangeOrderDesc'] = self.change_order_desc

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias

        if self.custom_image_network_type is not None:
            result['CustomImageNetworkType'] = self.custom_image_network_type

        if self.deploy is not None:
            result['Deploy'] = self.deploy

        if self.dotnet is not None:
            result['Dotnet'] = self.dotnet

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.empty_dir_desc is not None:
            result['EmptyDirDesc'] = self.empty_dir_desc

        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas

        if self.enable_cpu_burst is not None:
            result['EnableCpuBurst'] = self.enable_cpu_burst

        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route

        if self.enable_namespace_agent_version is not None:
            result['EnableNamespaceAgentVersion'] = self.enable_namespace_agent_version

        if self.enable_new_arms is not None:
            result['EnableNewArms'] = self.enable_new_arms

        if self.enable_prometheus is not None:
            result['EnablePrometheus'] = self.enable_prometheus

        if self.enable_sidecar_resource_isolated is not None:
            result['EnableSidecarResourceIsolated'] = self.enable_sidecar_resource_isolated

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.gpu_config is not None:
            result['GpuConfig'] = self.gpu_config

        if self.html is not None:
            result['Html'] = self.html

        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        result['InitContainersConfig'] = []
        if self.init_containers_config is not None:
            for k1 in self.init_containers_config:
                result['InitContainersConfig'].append(k1.to_map() if k1 else None)

        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args

        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options

        if self.jdk is not None:
            result['Jdk'] = self.jdk

        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.loki_configs is not None:
            result['LokiConfigs'] = self.loki_configs

        if self.max_surge_instance_ratio is not None:
            result['MaxSurgeInstanceRatio'] = self.max_surge_instance_ratio

        if self.max_surge_instances is not None:
            result['MaxSurgeInstances'] = self.max_surge_instances

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.micro_registration is not None:
            result['MicroRegistration'] = self.micro_registration

        if self.micro_registration_config is not None:
            result['MicroRegistrationConfig'] = self.micro_registration_config

        if self.microservice_engine_config is not None:
            result['MicroserviceEngineConfig'] = self.microservice_engine_config

        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances

        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc

        if self.mount_host is not None:
            result['MountHost'] = self.mount_host

        if self.nas_configs is not None:
            result['NasConfigs'] = self.nas_configs

        if self.nas_id is not None:
            result['NasId'] = self.nas_id

        if self.new_sae_version is not None:
            result['NewSaeVersion'] = self.new_sae_version

        if self.oidc_role_name is not None:
            result['OidcRoleName'] = self.oidc_role_name

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

        if self.php is not None:
            result['Php'] = self.php

        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location

        if self.php_config is not None:
            result['PhpConfig'] = self.php_config

        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.pvtz_discovery_svc is not None:
            result['PvtzDiscoverySvc'] = self.pvtz_discovery_svc

        if self.python is not None:
            result['Python'] = self.python

        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.secret_mount_desc is not None:
            result['SecretMountDesc'] = self.secret_mount_desc

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_tags is not None:
            result['ServiceTags'] = self.service_tags

        result['SidecarContainersConfig'] = []
        if self.sidecar_containers_config is not None:
            for k1 in self.sidecar_containers_config:
                result['SidecarContainersConfig'].append(k1.to_map() if k1 else None)

        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs

        if self.sls_log_env_tags is not None:
            result['SlsLogEnvTags'] = self.sls_log_env_tags

        if self.startup_probe is not None:
            result['StartupProbe'] = self.startup_probe

        if self.swimlane_pvtz_discovery_svc is not None:
            result['SwimlanePvtzDiscoverySvc'] = self.swimlane_pvtz_discovery_svc

        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config

        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

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

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('AlbIngressReadinessGate') is not None:
            self.alb_ingress_readiness_gate = m.get('AlbIngressReadinessGate')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')

        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')

        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')

        if m.get('ChangeOrderDesc') is not None:
            self.change_order_desc = m.get('ChangeOrderDesc')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')

        if m.get('CustomImageNetworkType') is not None:
            self.custom_image_network_type = m.get('CustomImageNetworkType')

        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')

        if m.get('Dotnet') is not None:
            self.dotnet = m.get('Dotnet')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('EmptyDirDesc') is not None:
            self.empty_dir_desc = m.get('EmptyDirDesc')

        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')

        if m.get('EnableCpuBurst') is not None:
            self.enable_cpu_burst = m.get('EnableCpuBurst')

        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')

        if m.get('EnableNamespaceAgentVersion') is not None:
            self.enable_namespace_agent_version = m.get('EnableNamespaceAgentVersion')

        if m.get('EnableNewArms') is not None:
            self.enable_new_arms = m.get('EnableNewArms')

        if m.get('EnablePrometheus') is not None:
            self.enable_prometheus = m.get('EnablePrometheus')

        if m.get('EnableSidecarResourceIsolated') is not None:
            self.enable_sidecar_resource_isolated = m.get('EnableSidecarResourceIsolated')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('GpuConfig') is not None:
            self.gpu_config = m.get('GpuConfig')

        if m.get('Html') is not None:
            self.html = m.get('Html')

        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        self.init_containers_config = []
        if m.get('InitContainersConfig') is not None:
            for k1 in m.get('InitContainersConfig'):
                temp_model = main_models.InitContainerConfig()
                self.init_containers_config.append(temp_model.from_map(k1))

        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')

        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')

        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')

        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('LokiConfigs') is not None:
            self.loki_configs = m.get('LokiConfigs')

        if m.get('MaxSurgeInstanceRatio') is not None:
            self.max_surge_instance_ratio = m.get('MaxSurgeInstanceRatio')

        if m.get('MaxSurgeInstances') is not None:
            self.max_surge_instances = m.get('MaxSurgeInstances')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MicroRegistration') is not None:
            self.micro_registration = m.get('MicroRegistration')

        if m.get('MicroRegistrationConfig') is not None:
            self.micro_registration_config = m.get('MicroRegistrationConfig')

        if m.get('MicroserviceEngineConfig') is not None:
            self.microservice_engine_config = m.get('MicroserviceEngineConfig')

        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')

        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')

        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')

        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')

        if m.get('NasConfigs') is not None:
            self.nas_configs = m.get('NasConfigs')

        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('OidcRoleName') is not None:
            self.oidc_role_name = m.get('OidcRoleName')

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

        if m.get('Php') is not None:
            self.php = m.get('Php')

        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')

        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')

        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('PvtzDiscoverySvc') is not None:
            self.pvtz_discovery_svc = m.get('PvtzDiscoverySvc')

        if m.get('Python') is not None:
            self.python = m.get('Python')

        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('SecretMountDesc') is not None:
            self.secret_mount_desc = m.get('SecretMountDesc')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceTags') is not None:
            self.service_tags = m.get('ServiceTags')

        self.sidecar_containers_config = []
        if m.get('SidecarContainersConfig') is not None:
            for k1 in m.get('SidecarContainersConfig'):
                temp_model = main_models.SidecarContainerConfig()
                self.sidecar_containers_config.append(temp_model.from_map(k1))

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('SlsLogEnvTags') is not None:
            self.sls_log_env_tags = m.get('SlsLogEnvTags')

        if m.get('StartupProbe') is not None:
            self.startup_probe = m.get('StartupProbe')

        if m.get('SwimlanePvtzDiscoverySvc') is not None:
            self.swimlane_pvtz_discovery_svc = m.get('SwimlanePvtzDiscoverySvc')

        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')

        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        return self

