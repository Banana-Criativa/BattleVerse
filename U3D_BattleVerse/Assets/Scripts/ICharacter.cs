using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public interface ICharacter
{
    string FirstName { get; set; }
    string LastName { get; set; }
    string FullName { get; set; }
    string MainAlias { get; set; }
    string[] AliasList { get; set; }
}
