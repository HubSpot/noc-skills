package com.hubspot.NocSkillsAPI;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.yammer.dropwizard.config.Configuration;
import org.hibernate.validator.constraints.NotEmpty;


public class NocSkillsAPIConfiguration extends Configuration {
  @NotEmpty
  @JsonProperty
  private String mongoHost;
  
  @JsonProperty
  private Integer mongoPort;
  
  @NotEmpty
  @JsonProperty
  private String mongoDBName;
  
  
  public String getMongoHost() {
    return mongoHost;
  }
  
  public int getMongoPort() {
    return mongoPort;
  }
  
  public String getMongoDBName() {
    return mongoDBName;
  }
  

}
