package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseRegistion extends GameResponse {

    private String username;
    private String password;

    public ResponseRegistion() {
        responseCode = Constants.SMSG_REGISTER;
    }

    @Override
    public byte[] constructResponseInBytes() {
      int number == 0;
      
      GamePacket packet = new GamePacket(responseCode);
      packet.addInt32(number);
      return packet.getBytes();
    }

    public String getUsername() {
      return username;
    }

    public void setUsername(String username) {
      this.username = username;
    }

    public String getPassword() {
      return password;
    }

    public void setPassword(String password) {
      this.password = password;
    }
}
