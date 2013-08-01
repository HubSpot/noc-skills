package com.hubspot.NocSkillsAPI;

import com.google.code.morphia.annotations.Entity;
import com.google.code.morphia.annotations.Id;
import org.bson.types.ObjectId;

@Entity
public class Reason {
  @Id private ObjectId id;
  
  private String name;
  private String reason;
  private String imageURL;
  
  public String getName() {
    return this.name;
  }
  
  public void setName(String name) {
    this.name = name;
  }
  
  public String getReason() {
    return this.reason;
  }
  
  public void setReason(String reason) {
    this.reason = reason;
  }
  
  public String getImageURL() {
    return this.imageURL;
  }
  
  public void setImageURL(String imageURL) {
    this.imageURL = imageURL;
  }
  
}
